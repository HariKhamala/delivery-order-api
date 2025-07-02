from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.vendor import VendorCreate, VendorDTO
from app.services import vendor_service
from app.database import SessionLocal

router = APIRouter(prefix="/vendors")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VendorDTO)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    return vendor_service.create_vendor(db, vendor)

@router.get("/", response_model=list[VendorDTO])
def get_all_vendors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return vendor_service.get_vendors(db, skip, limit)
