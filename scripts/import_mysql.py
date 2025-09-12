#import library from python
from sqlalchemy import create_engine
import pandas as pd

#import dataset from directory data
path = r"D:\Portofolio\Portofolio Mobile Phone Sales\data\mobile_data.csv"
data = pd.read_csv(path)

#show dataset using print
print(data)

#make a connection with MySQL with validation user
user = "root"
password = ""
host = "127.0.0.1"
port = 3306
database = "sales"

#make a engine to connect with MySQL
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

#upload dataset to database
data.to_sql(
    "mobiles",
    engine,
    index=False,
    if_exists="replace",
    chunksize=5000
)

