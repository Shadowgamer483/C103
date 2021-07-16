import pandas as pd
import plotly_express as px

df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\C103/line_chart.csv")
fig=px.line(df,x="Year",y="Per capita income",color="Country",title="Per capita of countrys by year")
fig.show()