from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://nihal1:Nihal123@cluster0.nlq4e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new clinet to connect ot server
client=MongoClient(uri)

#create database name colection name
DATABASE_NAME="mrnj"
COLLECTION_NAME="waferfault"

df=pd.read_csv(r"C:\Users\Lenovo\Desktop\SensorProject\notebooks\src\wafer.csv")

df=df.drop("Unnamed: 0",axis=1)
# df.head()
json_record=list(json.loads(df.T.to_json()).values())
# type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)