import pandas as pd
import numpy as np
df=pd.read_csv("income_csv.csv")
print(df)
"""print(df)
income_dc=df.columns#all data columns
print(income_dc)
#first two columns from the income set
print(income_dc[:2])
#find data types for all the columns
print(df.dtypes)
df.Y2008 = df.Y2008.astype(float)#convert integer type into float type
print(df.dtypes)
print("Total Number of Rows and Columns",df.shape)
print("Total Number of Rows and Columns",df.shape[0])
print("Total Number of Rows and Columns",df.shape[1])
print("First five records from incole dataset")
print(df.head())
print(df.tail())
print("First three rows   records from incole dataset")
print(df.head(3))
print("Last three rows   records from incole dataset")
print(df.tail(3))
print(df.iloc[0:5])
print(df[0:5])
#Random Sampling
data=df.sample(frac=0.1)
print(data)"""
print("Distinct values of the column Index")
u_values=df.Notation.unique()
print(u_values,len(u_values))
#biviberage requency distribution
print(pd.crosstab(df.Notation,df.State))
#creating Frequency distribution based on the Index
print(df.Notation.value_counts(ascending=True))
#multiple columns By Name
print(df[["Notation","State","Y2008"]])
print(df.loc[:,["Notation","State","Y2008"]])
print(df.loc[:6,["Notation","State","Y2008"]])
print(df.iloc[0:5,0:4])
df["difference"]=df.Y2008-df.Y2009
print(df["difference"])
df["difference2"]=df.eval("Y2008-Y2009")
print(df["difference2"])
