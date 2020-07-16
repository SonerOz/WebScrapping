import pymongo
from pymongo import MongoClient
import pandas as pd 
import json 

######### Connect to your database (I used the one on the cloud) #########
myclient = pymongo.MongoClient("mongodb+srv://********************************.mongodb.net/Job-app?retryWrites=true&w=majority")


####### Create DB #######
mydb = myclient["Dataset"]

####### Create Collection ######
mycollection = mydb["Jobs"]

######### Read CSV File ########
df = pd.read_csv("Jobs.csv", encoding = "ISO-8859-1")
data = df.to_dict(orient='records')

######### Insert your data to MongoDB ##########
mycollection.insert_many(data, ordered=False)



