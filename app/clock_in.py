from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from app.models import ClockInRecord, UpdateClockInRecord
from app.database import db, get_item_by_id
from datetime import datetime

router = APIRouter()

clock_in_collection = db["clock_in"]

# 1. Create Clock-In Record (POST)
@router.post("/clock-in/")
async def create_clock_in(record: ClockInRecord):
    record_dict = record.dict()
    result = clock_in_collection.insert_one(record_dict)
    record_dict["_id"] = str(result.inserted_id)
    return record_dict

# 2. Get Clock-In Record by ID (GET)
@router.get("/clock-in/{id}")
async def get_clock_in(id: str):
    return get_item_by_id(clock_in_collection, id)

# 3. Filter Clock-In Records (GET)
@router.get("/clock-in/filter")
async def filter_clock_in(email: str = None, location: str = None, insert_datetime: datetime = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gt": insert_datetime}
    
    records = list(clock_in_collection.find(query))
    return [{"_id": str(record["_id"]), **record} for record in records]

# 4. Update Clock-In Record by ID (PUT)
@router.put("/clock-in/{id}")
async def update_clock_in(id: str, record: UpdateClockInRecord):
    updated_data = {k: v for k, v in record.dict().items() if v is not None}
    if len(updated_data) >= 1:
        result = clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        if result.matched_count == 1:
            return get_item_by_id(clock_in_collection, id)
    raise HTTPException(status_code=404, detail="Clock-in record not found")

# 5. Delete Clock-In Record by ID (DELETE)
@router.delete("/clock-in/{id}")
async def delete_clock_in(id: str):
    result = clock_in_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Clock-in record deleted successfully"}
    raise HTTPException(status_code=404, detail="Clock-in record not found")
