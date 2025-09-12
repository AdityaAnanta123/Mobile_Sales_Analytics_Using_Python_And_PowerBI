#import library from python 
import pandas as pd
import numpy as np

#import file from directory data
path = r"D:\Portofolio\Portofolio Mobile Phone Sales\data\mobile_sales_data.csv"
data = pd.read_csv(path)

#show data from dataset mobile_sales_data
print(data)

#show top 10 data from dataset mobile_sales_data
print(data.head(10))

#show information about dataset
print(data.info())

#check missing values in dataset
print(data.isna().sum())

#imputation using mode to handle missing values based on column brand
data['SSD'] = data.groupby('Brand')['SSD'].transform(lambda x: x.fillna(x.mode()[0]))
data['Core Specification'] = data.groupby('Brand')['Core Specification'].transform(lambda x: x.fillna(x.mode()[0]))

#check again missing values in dataset
print(data.isna().sum())

#export result of preprocessing to new dataset
new_path = r"D:\Portofolio\Portofolio Mobile Phone Sales\data\mobile_data.csv"
data.to_csv(new_path, index=False)