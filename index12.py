import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    {"name": "Gou", "address": "Mango st 305"},
    {"name": "Suni", "address": "Sky st 405"},
    {"name": "Akho", "address": "Mountain st 315"},
    {"name": "Kus", "address": "Ocean st 3"},
    {"name": "Swa", "address": "Grass st 5"},
    {"name": "Pav", "address": "Valley st 305"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)




