from pydantic import BaseModel

class ParcelDTO(BaseModel):
    customer_name: str
    delivery_address: str
    tracking_number: str
