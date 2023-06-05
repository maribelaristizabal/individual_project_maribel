from pydantic import BaseModel, Field

from typing import Optional 

class Product(BaseModel):
        id: Optional[int] = None
        name: str = Field(max_length=30,min_length=3,description="product name")
        brand: str = Field(max_length=30,min_length=1,description="brand name")
        description: str = Field(max_length=100,min_length=1,description="product description")
        price: int = Field(ge=1,le=50000,description="product price")
        entry_date: str  = Field(max_length=15,min_length=3,description="enter the date of entry of the product")
        availability: str = Field(max_length=25,min_length=3,description="enter product availability")
        available_quantity: int = Field(ge=1,le=10000,description="enter the quantity available")

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'rice',
                    'brand': 'roa',
                    'description':'selected rice',
                    'price': 150,
                    'entry_date':'09/05/2023',
                    'availability':'availability',
                    'available_quantity': 100
                }
            }