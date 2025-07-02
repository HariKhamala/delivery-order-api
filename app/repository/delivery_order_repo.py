from sqlalchemy.orm import Session
from app.models.delivery_order import DeliveryOrder
from app.models.vendor import Vendor
from app.schemas.delivery_order import DeliveryOrderCreate
from typing import List
from datetime import date

def create_order(db: Session, order: DeliveryOrderCreate):
    db_order = DeliveryOrder(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DeliveryOrder).offset(skip).limit(limit).all()

def get_orders_by_vendor_and_date(db: Session, vendor_id: int, order_date: date):
    return db.query(DeliveryOrder).filter(
        DeliveryOrder.vendor_id == vendor_id,
        DeliveryOrder.order_date == order_date
    ).all()
