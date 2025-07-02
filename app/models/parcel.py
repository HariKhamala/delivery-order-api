# In-memory model (not DB model)
from pydantic import BaseModel

class Parcel(BaseModel):
    customer_name: str
    delivery_address: str
    contact_number: str
    parcel_size: str
    parcel_weight: float
    tracking_number: str
