from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class Item(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: Optional[datetime] = Field(default_factory=datetime.utcnow)

class UpdateItem(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[datetime]

class ClockInRecord(BaseModel):
    email: EmailStr
    location: str
    insert_datetime: Optional[datetime] = Field(default_factory=datetime.utcnow)

class UpdateClockInRecord(BaseModel):
    email: Optional[EmailStr]
    location: Optional[str]
