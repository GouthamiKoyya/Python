import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mango st 305" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
