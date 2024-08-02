import pandas as pd
import numpy as np
df=pd.read_csv("income_csv.csv")
df.ratio=df.Y2008/df.Y2009
print(df.ratio)
data=df.assign(ratio=(df.Y2008/df.Y2009))
print(data.head())
print(data.describe())#for numeric variables
print(data.describe(include=['object']))#for numeric variables
print(df.Y2008.mean(),df.Y2008.median())
print(df.Y2008.agg(["mean","median"]))
print(df.loc[:,["Y2008","Y2009"]].max())
print(df.Y2008.min())
print(df.loc[df.Notation=="A"])
print(df.groupby("Notation")[["Y2008","Y2009"]].min())
print(df.groupby("Notation")[["Y2008","Y2009"]].agg(["min","max","mean"]))
dt=df.groupby("Notation").agg({"Y2008":["min","max"],"Y2009":"mean"})
dt.columns=['Y2008_min','2008_max','2009_mean']
print(dt)
print(df.groupby(["Notation","State"]).agg({"Y2002":[min,max],"Y2003":"mean"}))
print(df.loc[df.Notation=="A"])
print(df.loc[df.Notation=="A","State"])