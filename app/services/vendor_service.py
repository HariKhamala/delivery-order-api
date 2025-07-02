from sqlalchemy.orm import Session
from app.schemas.vendor import VendorCreate
from app.repository import vendor_repo

def create_vendor(db: Session, vendor: VendorCreate):
    return vendor_repo.create_vendor(db, vendor)

def get_vendors(db: Session, skip: int = 0, limit: int = 10):
    return vendor_repo.get_all_vendors(db, skip, limit)
