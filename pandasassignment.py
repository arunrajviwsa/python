import pandas as pd
import numpy as np
df=pd.read_csv("iris_csv.csv")
print("*"*30,"Exercise 1: Load and Inspect the Data\n","*"*30)
print("1.Loading data from Csv\n",df)
print("2.First 10 records from Csv\n",df.head(10))
print("3.Data types of each column.\n",df.dtypes)
print("*"*30,"Excercise 2: Summary Statistics","*"*30)
print("1.Statictics",df.describe())
print("2. Mean sepal length for each species.\n",df["Sepal.Length"].mean())
print("*"*30,"Exercise 3: Data Cleaning","*"*30)
species = pd.DataFrame(df)
print("Check for missing values \n",species.isnull().sum())
species.fillna({"Sepal.Length":species["Sepal.Length"].mean(),"Sepal.Width":species["Sepal.Width"].mean(),"Petal.Length":species["Petal.Length"].mean(),"Petal.Width":species["Petal.Width"].mean()}, inplace=True)
print("Replace any missing values with the mean of the respective column\n",species)
print("*"*30,"Exercise 4: Data Filtering","*"*30)
print("Filter the dataset to include only rows where the sepal length is greater than 5.0.\n",df.loc[(df["Sepal.Length"] > 5.0),:])
print("Filter the dataset to include only rows of the species 'Setosa'.\n",df.loc[df["Species"]=="setosa"])
print("*"*30,"Exercise 5: Data Aggregation","*"*30)
print("mean, median, and standard deviation of petal length for each species\n",print(df.groupby(["Species"]).agg({"Petal.Length":["mean","median","std"]})))
print("Count the number of occurrences of each species\n",print(df.groupby(["Species"]).count()))
highest_average= df.groupby(["Species"]).agg({"Sepal.Width":"mean"})

print(f"species with the highest average sepal width: {highest_average.idxmax()}")
df.ratio = df["Petal.Length"]/df["Petal.Width"]
print(df.ratio)
print("*"*30,"Exercise 6: Data Transformation","*"*30)

data = df.assign(ratio=df["Petal.Length"]/df["Petal.Width"])
print(data)
print("*"*30,"Exercise 7: Advanced Data Aggregation","*"*30)
percentile = df.groupby('Species')['Sepal.Length'].quantile([0.25, 0.5, 0.75]).unstack()
percentile.column = ['25th_percentiles', '50th_percentiles ', '75th_percentiles ']
print("25th, 50th, and 75th percentiles of sepal length for each species.")
print(percentile)
data = df.groupby('Species')["Petal.Length"].agg(lambda x: x.max() - x.min())
print("Range (max - min) of petal length for each species.",data)
print("Exercise 8: Merging and Joining")
Zodiac_data = pd.DataFrame({"Names":["luther","martine"],
                            "Habitat": ["morning","even"],
                            "Section": ["one","two"]})
print("new DataFrame with additional information about each species\n",Zodiac_data)

iris = pd.concat([df,Zodiac_data],axis=1)
print("Merge new DataFrame with the original Iris DataFrame\n",iris)

def size_check(row):
    if row["Petal.Length"] >= 5:
        return "large"
    elif row["Petal.Length"] >=3 and row["Petal.Length"] <5:
        return "Medium"
    else:
        return "small"
species['Flower.Size'] = species.apply(size_check, axis=1)
print("Exercise 9: Applying Custom Functions\n")
print("custom function that categorizes flowers as small, medium, or large based on petal length\n")
print(species)
print(species)gugi





