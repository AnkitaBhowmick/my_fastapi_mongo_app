from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from app.models import Item, UpdateItem
from app.database import db, get_item_by_id
from datetime import datetime

router = APIRouter()

items_collection = db["items"]

# 1. Create an Item (POST)
@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    result = items_collection.insert_one(item_dict)
    item_dict["_id"] = str(result.inserted_id)
    return item_dict

# 2. Get Item by ID (GET)
@router.get("/items/{id}")
async def get_item(id: str):
    return get_item_by_id(items_collection, id)

# 3. Filter Items (GET)
@router.get("/items/filter")
async def filter_items(email: str = None, expiry_date: datetime = None, insert_date: datetime = None, quantity: int = None):
    query = {}
    if email:
        query["email"] = email
    if expiry_date:
        query["expiry_date"] = {"$gt": expiry_date}
    if insert_date:
        query["insert_date"] = {"$gt": insert_date}
    if quantity:
        query["quantity"] = {"$gte": quantity}
    
    items = list(items_collection.find(query))
    return [{"_id": str(item["_id"]), **item} for item in items]

# 4. MongoDB Aggregation (GET)
@router.get("/items/aggregation")
async def aggregate_items():
    pipeline = [
        {
            "$group": {
                "_id": "$email",
                "count": {"$sum": 1}
            }
        }
    ]
    aggregation = list(items_collection.aggregate(pipeline))
    return [{"email": item["_id"], "count": item["count"]} for item in aggregation]

# 5. Update Item by ID (PUT)
@router.put("/items/{id}")
async def update_item(id: str, item: UpdateItem):
    updated_data = {k: v for k, v in item.dict().items() if v is not None}
    if len(updated_data) >= 1:
        result = items_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        if result.matched_count == 1:
            return get_item_by_id(items_collection, id)
    raise HTTPException(status_code=404, detail="Item not found")

# 6. Delete Item by ID (DELETE)
@router.delete("/items/{id}")
async def delete_item(id: str):
    result = items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
