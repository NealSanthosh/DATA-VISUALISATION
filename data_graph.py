import plotly_express as px
import pandas as pd


df =  pd.read_csv("data.csv")
fig =px.scatter(df, x = "Date", y ="Cases", color = "Country", title = "DATA VISUALISATION")
fig.show()
