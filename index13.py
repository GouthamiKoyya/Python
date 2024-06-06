import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    { "_id":1, "name": "Gou", "address": "Mango st 305"},
    { "_id":2, "name": "Suni", "address": "Sky st 405"},
    {  "_id":3, "name": "Akho", "address": "Mountain st 315"},
    {  "_id":4, "name": "Kus", "address": "Ocean st 3"},
    { "_id":5, "name": "Swa", "address": "Grass st 5"},
    { "_id":6, "name": "Pav", "address": "Valley st 30"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)




