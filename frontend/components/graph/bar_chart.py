import plotly.express as px
from frontend.utils.dataframe import df


### PM2.5 when rain and not rain

pm25_rain_stats = df.groupby('is_rain')['pm2_5_atm'].agg(['mean', 'median', 'min', 'max', 'std']).reset_index()
pm25_rain_stats['is_rain'] = pm25_rain_stats['is_rain'].map({True: 'Rain', False: 'No Rain'})
df['is_rain_label'] = df['is_rain'].map({True: 'Rain', False: 'No Rain'})

pm2_5_rain = px.bar(pm25_rain_stats,
             x='is_rain',
             y='mean',
             title='pm 2.5 atm levels: Rain vs No Rain',
             labels={'is_rain': 'Rain Condition', 'mean': 'Average PM 2.5 (μg/m^3)'})
pm2_5_rain.update_layout(width=800, height=600)

df.drop('is_rain_label', axis=1, inplace=True)
