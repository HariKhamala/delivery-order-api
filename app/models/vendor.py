from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class SubscriptionType(str, enum.Enum):
    NORMAL = "NORMAL"
    PRIME = "PRIME"
    VIP = "VIP"

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    subscription_type = Column(Enum(SubscriptionType))
    
    delivery_orders = relationship("DeliveryOrder", back_populates="vendor")
