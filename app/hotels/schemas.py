from fastapi import Query
from pydantic import BaseModel
from typing import List, Any
from typing import Optional


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: List[Any]
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True


class HotelSearchArgs:
    def __init__(
        self,
        name: str,
        location: str,
        services: List[str] = Query(..., description="List of cities or locations"),
        rooms_quantity: Optional[int] = None, 
        image_id: Optional[int] = None,        
    ):
        self.name = name
        self.location = location
        self.services = services
        self.rooms_quantity = rooms_quantity
        self.image_id = image_id
    