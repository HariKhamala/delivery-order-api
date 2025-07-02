from fastapi import FastAPI, Depends, HTTPException
from app.database import engine
from app.models.vendor import Base as VendorBase
from app.models.delivery_order import Base as OrderBase

from app.controllers import vendor_controller, delivery_order_controller

app = FastAPI()

VendorBase.metadata.create_all(bind=engine)
OrderBase.metadata.create_all(bind=engine)

app.include_router(vendor_controller.router)
app.include_router(delivery_order_controller.router)

@app.get("/")
def root():
    return {"message": "Delivery Order API is running!"}

from fastapi.security import OAuth2PasswordRequestForm
from app import auth

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = auth.create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

from app.auth import get_current_user

@app.get("/secure-data")
def read_secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user['username']}!"}


