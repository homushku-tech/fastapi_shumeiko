from fastapi import APIRouter, Depends
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import RoomsSearchArgs, SRooms
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix="/{hotels_id}/rooms",
    tags=["Номера в отели"],
)

@router.get("")
async def get_rooms() -> list[SRooms]:
    return await RoomsDAO.find_all()

@router.post("")
async def post_rooms(
    hotel_id: int,
    room_data: RoomsSearchArgs = Depends()
):
    new_room = await RoomsDAO.add(hotel_id = hotel_id, **room_data.__dict__)
    return new_room
