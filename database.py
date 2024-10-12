from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi import HTTPException

# MongoDB connection string
client = MongoClient("mongodb+srv://mongodb:<db_password>@cluster0.jvo61.mongodb.net/")
db = client["mydatabase"]

def get_item_by_id(collection, id):
    item = collection.find_one({"_id": ObjectId(id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item["_id"] = str(item["_id"])
    return item
