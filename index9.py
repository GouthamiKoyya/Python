import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/' )
mydb = myclient['mydatabase']
mycol = mydb["customers"]
mydict = {"name": "Gouthami", "address": "Highway 17" }
x = mycol.insert_one(mydict)
print(x)
