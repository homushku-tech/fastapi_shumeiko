from fastapi import APIRouter, Depends

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotels
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/{hotels_id}/rooms",
    tags=["Номера в отели"],
)

@router.get("")
async def get_rooms(user: Users = Depends(get_current_user)) -> list[SHotels]:
    return await HotelsDAO.find_all()