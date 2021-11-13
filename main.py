import csv
import pandas as pd
import plotly.figure_factory as ff

df= pd.read_csv("data.csv")
avg=df[("Avg Rating")].tolist()
fig=ff.create_distplot([avg],["average"])
fig.show()