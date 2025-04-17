import plotly.express as px
from frontend.utils.dataframe import df
from .stats import corr

### Correlation of numerical attributes

corr = px.imshow(corr, zmin=-1, text_auto=True, width=800, height=800)
