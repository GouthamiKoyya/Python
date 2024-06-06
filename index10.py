import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

mydict = { "name": "Gouthami", "address": "Vizag 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)
