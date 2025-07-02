from pydantic import BaseModel
from enum import Enum

class SubscriptionType(str, Enum):
    NORMAL = "NORMAL"
    PRIME = "PRIME"
    VIP = "VIP"

class VendorBase(BaseModel):
    name: str
    subscription_type: SubscriptionType

class VendorCreate(VendorBase):
    pass

class VendorDTO(VendorBase):
    id: int

    class Config:
        orm_mode = True
