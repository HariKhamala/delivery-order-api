from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.schemas.delivery_order import DeliveryOrderCreate, DeliveryOrderDTO
from app.services import delivery_order_service
from app.database import SessionLocal
from datetime import date
import shutil
import os

router = APIRouter(prefix="/orders")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=DeliveryOrderDTO)
def upload_order(
    order_date: date = Form(...),
    vendor_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    order = DeliveryOrderCreate(order_date=order_date, vendor_id=vendor_id, file_path=file_path)
    return delivery_order_service.create_order(db, order)

@router.get("/", response_model=list[DeliveryOrderDTO])
def get_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return delivery_order_service.get_orders(db, skip, limit)

@router.get("/filter", response_model=list[DeliveryOrderDTO])
def get_orders_by_vendor_and_date(vendor_id: int, order_date: date, db: Session = Depends(get_db)):
    return delivery_order_service.get_orders_by_vendor_and_date(db, vendor_id, order_date)
