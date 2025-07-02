from pydantic import BaseModel
from datetime import date

class DeliveryOrderCreate(BaseModel):
    order_date: date
    vendor_id: int
    file_path: str

class DeliveryOrderDTO(BaseModel):
    id: int
    order_date: date
    vendor_name: str
    file_path: str

    class Config:
        orm_mode = True
