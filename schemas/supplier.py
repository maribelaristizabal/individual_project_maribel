from pydantic import BaseModel, Field
from typing import Optional


class Supplier(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=25,min_length=2, description="provider's name")
    address: str = Field(max_length=100,min_length=5,description="enter your address")
    phone: int = Field(ge=10,le=20,description="enter your phone")
    email: str = Field(max_length=300,min_length=20,description="enter your email")
    class Config:
        schema_extra =  {
            "example":{
                "id":1,
                "name":'Ana',
                "address":'california 234',
                "phone" : 3123345535,
                "email" : "holamundo@gmail.com"
            }
        }