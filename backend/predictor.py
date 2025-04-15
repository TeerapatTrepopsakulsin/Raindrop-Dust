from . import crud
from .database import SessionLocal

from sklearn.preprocessing import (
    OneHotEncoder, StandardScaler
)
import pandas as pd
import numpy as np
from sklearn.svm import SVR

snd_col = [
    'id',
    'ts',
    'lat',
    'lon',
    'temp',
    'hum',
    'weather_main',
    'weather_con',
    'wind_spd',
    'cloud',
    'rain'
]
pmr_col = [
    'id',
    'ts',
    'temp',
    'light',
    'hum',
    'aqi',
    'pm1_0',
    'pm2_5',
    'pm10_0',
    'pm1_0_atm',
    'pm2_5_atm',
    'pm10_0_atm',
    'pcnt_0_3',
    'pcnt_0_5',
    'pcnt_1_0',
    'pcnt_2_5',
    'pcnt_5_0',
    'pcnt_10_0'
]
db = SessionLocal()
snd_data = [
    {col: getattr(item, col) for col in snd_col}
    for item in crud.get_raw_secondary(db)
]
pmr_data = [
    {col: getattr(item, col) for col in pmr_col}
    for item in crud.get_raw_primary(db)
]
snd_df = pd.DataFrame(snd_data,  columns=snd_col)
pmr_df = pd.DataFrame(pmr_data, columns=pmr_col)
db.close()


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
    target_df = df[df['ts']==target]
    return target_df[f].values[0] if len(target_df) > 0 else np.nan

for col in ['pm2_5_atm', 'pm10_0_atm', 'aqi']:
    for i in [1, 3, 6, 12, 24, 72]:
        df[f'{col}_lag{i}h'] = df.apply(lambda x: get_lagged_data(x, np.timedelta64(i, 'h'), col), axis=1)

# Lead Features
def get_lead_data(x, t: np.timedelta64, f: str):
    """ Get the lead data of the specify lead timedelta and feature."""
    target = x['ts'] + t
    target_df = df[df['ts']==target]
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

# Encoding
numerical = [
    "light",
    "aqi",
    "pm1_0",
    "pm2_5",
    "pm10_0",
    "pm1_0_atm",
    "pm2_5_atm",
    "pm10_0_atm",
    "pcnt_0_3",
    "pcnt_0_5",
    "pcnt_1_0",
    "pcnt_2_5",
    "pcnt_5_0",
    "pcnt_10_0",
    "min_temp",
    "max_temp",
    "lat",
    "lon",
    "wind_spd",
    "cloud",
    "rain"
]

ratio = [
    "light",
    "pm1_0",
    "pm2_5",
    "pm10_0",
    "pm1_0_atm",
    "pm2_5_atm",
    "pm10_0_atm",
    "pcnt_0_3",
    "pcnt_0_5",
    "pcnt_1_0",
    "pcnt_2_5",
    "pcnt_5_0",
    "pcnt_10_0",
    "min_temp",
    "max_temp",
    "wind_spd",
    "rain"
]

categorical = [
    'weather_main_Clouds',
    'weather_main_Mist',
    'weather_main_Rain',
    'weather_con_broken clouds',
    'weather_con_few clouds',
    'weather_con_heavy intensity rain',
    'weather_con_light rain',
    'weather_con_mist',
    'weather_con_moderate rain',
    'weather_con_overcast clouds',
    'weather_con_scattered clouds',
    'day_of_week_Friday',
    'day_of_week_Monday',
    'day_of_week_Saturday',
    'day_of_week_Sunday',
    'day_of_week_Thursday',
    'day_of_week_Tuesday',
    'day_of_week_Wednesday'
]

original_categorical = ["weather_main", "weather_con", "day_of_week"]

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

encoded = encoder.fit_transform(df[original_categorical]).astype(int)
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(original_categorical))
encoded_df.reset_index(drop=True, inplace=True)

df = pd.concat([df, encoded_df], axis=1)
df.drop(original_categorical, axis=1, inplace=True)

# Cyclical encoding
df['hour'] = np.sin(2 * np.pi * df['hour']/24)

orig_df = df.copy()

target_features = ['pm2_5_atm_lead1d',
                   'pm2_5_atm_lead3d',
                   'pm10_0_atm_lead1d',
                   'pm10_0_atm_lead3d',
                   'aqi_lead1d',
                   'aqi_lead3d']

def fit_model(init_df, model, target):
    # Preprocess Train
    df = init_df.copy()
    if 'ts' in df.columns:
        ts = df.pop('ts')

    df.dropna(inplace=True)

    # Split
    X_df = df.drop(target_features, axis=1)
    y_df = df[[target]]

    X = X_df.values
    y = y_df.values

    # Standardization
    standard_scaler = StandardScaler()
    X = standard_scaler.fit_transform(X)

    # Construct Model
    model.fit(X, y.ravel())

    return model


# def svr_predict(init_df, model, target):
#     # Preprocess Test (for Prediction)
#     for_predict_df = init_df.copy()
#     for_predict_df.drop(target_features, axis=1, inplace=True)
#     for_predict_df['ts'] = for_predict_df['ts'].dt.to_timestamp()
#     for_predict_df = for_predict_df[for_predict_df['ts'] >= (pd.Timestamp.now() - pd.Timedelta(days=3))]
#
#     for_predict_df.dropna(inplace=True)
#
#     prediction = pd.DataFrame()
#     prediction['ts'] = for_predict_df.pop('ts') + pd.Timedelta(days=3)
#
#     X = for_predict_df.values
#
#     standard_scaler = StandardScaler()
#     X = standard_scaler.fit_transform(X)
#
#     prediction[target] = model.predict(X)
#
#     prediction.reset_index(inplace=True)
#     prediction.drop('index', axis=1, inplace=True)
#
#     return prediction


# See in Data Analytics Colab to see how the model are tuned and constructed
svr_models= [
    {
        'target': 'pm2_5_atm_lead1d',
        'model': SVR(C=10, epsilon=0.01, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=10, epsilon=0.01, gamma=0.01, kernel='linear'), target='pm2_5_atm_lead1d'),
        'mse': 0.8452607265532294,
        'r2': 0.9950464669582851
    },
    {
        'target': 'pm2_5_atm_lead3d',
        'model': SVR(C=1, epsilon=0.01, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=1, epsilon=0.01, gamma=0.01, kernel='linear'), target='pm2_5_atm_lead3d'),
        'mse': 0.7589291448394546,
        'r2': 0.9945369556449393
        },
    {
        'target': 'pm10_0_atm_lead1d',
        'model': SVR(C=10, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=10, gamma=0.01, kernel='linear'),
                               target='pm10_0_atm_lead1d'),

        'mse': 5.836399745533746,
        'r2': 0.9799007294747933
    },
    {
        'target': 'pm10_0_atm_lead3d',
        'model': SVR(C=1, epsilon=0.01, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=1, epsilon=0.01, gamma=0.01, kernel='linear'),
                               target='pm10_0_atm_lead3d'),

        'mse': 3.592169515324138,
        'r2': 0.985140523330632},
    {
        'target': 'aqi_lead1d',
        'model': SVR(C=10, epsilon=0.01, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=10, epsilon=0.01, gamma=0.01, kernel='linear'),
                               target='aqi_lead1d'),

        'mse': 6.313332941706319,
        'r2': 0.9928753365024712},
    {
        'target': 'aqi_lead3d',
        'model': SVR(C=10, epsilon=0.2, gamma=0.01, kernel='linear'),
        'fit_model': fit_model(orig_df, model=SVR(C=10, epsilon=0.2, gamma=0.01, kernel='linear'),
                               target='aqi_lead3d'),

        'mse': 1.1572157503437615,
        'r2': 0.9983608655692785
     }
]

df = orig_df.copy()

def get_model(target: str):
    for model in svr_models:
        if model.get('target') == target:
            return model.get('fit_model')

class Predictor:
    PM25OneDay = get_model("pm2_5_atm_lead1d")
    PM25ThreeDay = get_model("pm2_5_atm_lead3d")
    PM10OneDay = get_model("pm10_0_atm_lead1d")
    PM10ThreeDay = get_model("pm10_0_atm_lead3d")
    AQIOneDay = get_model("aqi_lead1d")
    AQIThreeDay = get_model("aqi_lead3d")
    df = orig_df
    model = None

    @classmethod
    def get_1day_prediction(cls):
        pm2_5 = cls.predict("pm2_5_atm_lead1d")
        pm10_0 = cls.predict("pm10_0_atm_lead1d")
        aqi = cls.predict("aqi_lead1d")
        df = pd.merge(pm2_5, pm10_0, on='ts', how='inner')
        df = pd.merge(df, aqi, on='ts', how='inner')
        df.rename(columns={
            'ts': 'timestamp',
            'pm2_5_atm_lead1d': 'pm2_5',
            'pm10_0_atm_lead1d': 'pm10_0',
            'aqi_lead1d': 'aqi'
        }, inplace=True)
        return df.to_dict('records')

    @classmethod
    def get_3day_prediction(cls):
        pm2_5 = cls.predict("pm2_5_atm_lead3d")
        pm10_0 = cls.predict("pm10_0_atm_lead3d")
        aqi = cls.predict("aqi_lead3d")
        df = pd.merge(pm2_5, pm10_0, on='ts', how='inner')
        df = pd.merge(df, aqi, on='ts', how='inner')
        df.rename(columns={
            'ts': 'timestamp',
            'pm2_5_atm_lead3d': 'pm2_5',
            'pm10_0_atm_lead3d': 'pm10_0',
            'aqi_lead3d': 'aqi'
        }, inplace=True)
        return df.to_dict('records')

    @classmethod
    def predict(cls, target):
        if "3d" in target:
            days_pred = 3
        else:
            days_pred = 1

        cls.set_model(target)

        # Preprocess Test (for Prediction)
        for_predict_df = cls.df.copy()
        for_predict_df.drop(target_features, axis=1, inplace=True)
        for_predict_df['ts'] = for_predict_df['ts'].dt.to_timestamp()
        for_predict_df = for_predict_df[for_predict_df['ts'] >= (pd.Timestamp.now() - pd.Timedelta(days=days_pred))]

        for_predict_df.dropna(inplace=True)

        prediction = pd.DataFrame()
        prediction['ts'] = for_predict_df.pop('ts') + pd.Timedelta(days=days_pred)

        X = for_predict_df.values

        standard_scaler = StandardScaler()
        X = standard_scaler.fit_transform(X)

        prediction[target] = cls.model.predict(X)

        prediction.reset_index(inplace=True)
        prediction.drop('index', axis=1, inplace=True)

        return prediction

    @classmethod
    def set_model(cls, target):
        model_selection = {
            "pm2_5_atm_lead1d": cls.PM25OneDay,
            "pm2_5_atm_lead3d": cls.PM25ThreeDay,
            "pm10_0_atm_lead1d": cls.PM10OneDay,
            "pm10_0_atm_lead3d": cls.PM10ThreeDay,
            "aqi_lead1d": cls.AQIOneDay,
            "aqi_lead3d": cls.AQIThreeDay,
        }

        cls.model = model_selection[target]
