import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from .api import get_api_res


# Get Primary table
response = get_api_res("/raw/primary?limit=-1")
data = response.json()
pmr_df = pd.DataFrame(data)

# Get Primary table
response = get_api_res("/raw/secondary?limit=-1")
data = response.json()
snd_df = pd.DataFrame(data)

# Get Hourly table
response = get_api_res("/raw/hourly?limit=-1")
data = response.json()
hour_df = pd.DataFrame(data)


def preprocessing(primary: pd.DataFrame, secondary: pd.DataFrame) -> pd.DataFrame:
    pmr_df = primary.copy()
    snd_df = secondary.copy()

    pmr_df['ts'] = pd.to_datetime(pmr_df['ts'])
    snd_df['ts'] = pd.to_datetime(snd_df['ts'])

    # Identify outliers using IQR method
    def handle_outliers_iqr(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        return df

    # Primary Preprocessing
    pmr_df = handle_outliers_iqr(pmr_df, 'pm2_5_atm')
    pmr_df = handle_outliers_iqr(pmr_df, 'pm10_0_atm')

    pmr_df.drop('id', axis=1, inplace=True)
    pmr_df['bin_ts'] = pmr_df['ts'].dt.to_period('h')
    pmr_df.drop('ts', axis=1, inplace=True)

    grouped = pmr_df.groupby('bin_ts')
    pmr_interval = grouped.mean()
    pmr_interval['min_temp'] = grouped['temp'].min()
    pmr_interval['max_temp'] = grouped['temp'].max()

    # Secondary Preprocessing
    snd_df.drop('id', axis=1, inplace=True)
    snd_df['bin_ts'] = snd_df['ts'].dt.to_period('h')
    snd_df.drop('ts', axis=1, inplace=True)

    def get_mode(series):
        return series.mode().iloc[0] if not series.mode().empty else np.nan

    grouped = snd_df.groupby('bin_ts')
    numeric_cols = snd_df.select_dtypes(include='number').columns
    snd_interval = grouped[numeric_cols].mean()
    snd_interval['weather_main'] = grouped['weather_main'].apply(get_mode)
    snd_interval['weather_con'] = grouped['weather_con'].apply(get_mode)

    # Merge
    df = pd.merge(pmr_interval, snd_interval, on='bin_ts', how='inner', suffixes=('_pmr', '_snd'))
    df = df.reset_index().rename(columns={'bin_ts': 'ts'})
    binary_prefixes = ['weather_con_', 'weather_main_']
    binary_cols = [col for col in df.columns if any(col.startswith(prefix) for prefix in binary_prefixes)]
    df[binary_cols] = df[binary_cols].astype(int)

    # Feature Engineering

    # Lagged Features
    def get_lagged_data(x, t: np.timedelta64, f: str):
        """ Get the lagged data of the specify delayed timedelta and feature."""
        target = x['ts'] - t
        target_df = df[df['ts'] == target]
        return target_df[f].values[0] if len(target_df) > 0 else np.nan

    for col in ['pm2_5_atm', 'pm10_0_atm', 'aqi']:
        for i in [1, 3, 6, 12, 24, 72]:
            df[f'{col}_lag{i}h'] = df.apply(lambda x: get_lagged_data(x, np.timedelta64(i, 'h'), col), axis=1)

    # Lead Features
    def get_lead_data(x, t: np.timedelta64, f: str):
        """ Get the lead data of the specify lead timedelta and feature."""
        target = x['ts'] + t
        target_df = df[df['ts'] == target]
        return target_df[f].values[0] if len(target_df) > 0 else np.nan

    for col in ['pm2_5_atm', 'pm10_0_atm', 'aqi']:
        for i in [1, 3]:
            df[f'{col}_lead{i}d'] = df.apply(lambda x: get_lead_data(x, np.timedelta64(i, 'D'), col), axis=1)

    # Time-Series Features

    df['day_of_week'] = df['ts'].dt.to_timestamp().dt.day_name()
    df['hour'] = df['ts'].dt.hour

    # Weather Features

    df['is_rain'] = df['rain'] > 0

    # Drop Features

    df.drop(['temp_snd', 'hum_snd'], axis=1, inplace=True)

    df.reset_index(drop=True, inplace=True)

    # Cyclical encoding
    df['hour'] = np.sin(2 * np.pi * df['hour'] / 24)

    # Convert timestamp
    df['ts'] = df['ts'].dt.to_timestamp()

    return df


# Finalised data
df = preprocessing(primary=pmr_df, secondary=snd_df)

# Current data

today = pd.Timestamp.today()
today_df = df[df['ts'].dt.normalize() == today.normalize()]

week_df = df[df['ts'] >= today - pd.Timedelta(days=7)]
