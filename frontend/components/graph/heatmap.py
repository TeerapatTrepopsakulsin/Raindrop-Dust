import plotly.express as px
from .stats import corr, envi_corr


### Correlation of numerical attributes

corr = px.imshow(corr, zmin=-1, text_auto=True, width=800, height=800)

envi_corr = px.imshow(envi_corr, zmin=-1, text_auto=True, width=800, height=800)
