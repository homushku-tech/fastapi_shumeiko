import json
from pydantic import BaseModel

class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: json
    rooms_quantity: int
    image_id: int

    class Config:
        from_attributes = True


