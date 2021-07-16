import pandas as pd
import plotly_express as px

df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\C103/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country")
fig.show()