from sqlalchemy.orm import Session
from app.schemas.delivery_order import DeliveryOrderCreate
from app.repository import delivery_order_repo
from datetime import date

def create_order(db: Session, order: DeliveryOrderCreate):
    return delivery_order_repo.create_order(db, order)

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return delivery_order_repo.get_orders(db, skip, limit)

def get_orders_by_vendor_and_date(db: Session, vendor_id: int, order_date: date):
    return delivery_order_repo.get_orders_by_vendor_and_date(db, vendor_id, order_date)
