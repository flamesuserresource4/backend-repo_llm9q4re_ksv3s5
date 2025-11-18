"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional

# Example schemas (you can keep these or remove if not needed)
class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# MercRent collections
class Car(BaseModel):
    """
    Cars available for rent
    Collection name: "car"
    """
    brand: str = Field(..., description="Car brand, e.g., Mercedes")
    model: str = Field(..., description="Model name, e.g., C-Class")
    year: int = Field(..., ge=1980, le=2100, description="Manufacturing year")
    transmission: str = Field(..., description="Automatic or Manual")
    seats: int = Field(..., ge=1, le=9, description="Number of seats")
    fuel: str = Field(..., description="Fuel type, e.g., Petrol, Diesel, Hybrid, Electric")
    price_per_day: float = Field(..., ge=0, description="Daily rental price in USD")
    image_url: Optional[str] = Field(None, description="Marketing image URL")
    featured: bool = Field(False, description="Whether to highlight this car")

class Booking(BaseModel):
    """
    Customer bookings
    Collection name: "booking"
    """
    car_id: str = Field(..., description="ID of the car being booked")
    full_name: str = Field(..., description="Customer full name")
    email: str = Field(..., description="Customer email")
    pickup_location: str = Field(..., description="Pickup location")
    dropoff_location: str = Field(..., description="Dropoff location")
    pickup_date: str = Field(..., description="ISO date for pickup")
    dropoff_date: str = Field(..., description="ISO date for dropoff")
    notes: Optional[str] = Field(None, description="Optional notes for the booking")
