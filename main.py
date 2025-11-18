from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from database import db, create_document, get_documents
from schemas import Car, Booking

app = FastAPI(title="MercRent API", version="1.0.0")

# CORS so the frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CarCreate(Car):
    pass

class BookingCreate(Booking):
    pass

@app.get("/test")
def test():
    # Simple health/database check
    return {"ok": db is not None}

@app.post("/cars", response_model=dict)
def add_car(car: CarCreate):
    try:
        inserted_id = create_document("car", car)
        return {"id": inserted_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cars", response_model=List[dict])
def list_cars(brand: Optional[str] = None, featured: Optional[bool] = None, limit: int = 20):
    try:
        filters = {}
        if brand:
            filters["brand"] = brand
        if featured is not None:
            filters["featured"] = featured
        cars = get_documents("car", filters, limit)
        # Convert ObjectId to string for frontend safety
        for c in cars:
            c["id"] = str(c.pop("_id"))
        return cars
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/bookings", response_model=dict)
def create_booking(payload: BookingCreate):
    try:
        booking_id = create_document("booking", payload)
        return {"id": booking_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
