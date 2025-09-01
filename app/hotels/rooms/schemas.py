from typing import List, Any
from fastapi import Query
from pydantic import BaseModel
from typing import Optional

class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: List[Any]
    quantity: int
    image_id: int

    class Config:
        from_attributes = True


class SRoomInfo(SRooms):
    total_cost: int
    rooms_left: int

    class Config:
        from_attributes = True


class RoomsSearchArgs:
    def __init__(
        self,
        name: str,
        description: str,
        price: int, 
        services: List[str],
        quantity: Optional[int] = None, 
        image_id: Optional[int] = None,          
    ):

        self.name = name
        self.description = description
        self.price = price
        self.services = services
        self.quantity = quantity
        self.image_id = image_id
        