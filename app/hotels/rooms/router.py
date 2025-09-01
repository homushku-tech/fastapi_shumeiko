from datetime import date, datetime, timedelta
from fastapi_cache.decorator import cache
from fastapi import APIRouter, Depends, Query
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomInfo


router = APIRouter(
    prefix="/{hotel_id}/rooms",
    tags=["Номера в отели"],
)

@router.get("")
@cache(expire=20)
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> list[SRoomInfo]:
    rooms = await RoomsDAO.find_all(hotel_id, date_from, date_to)
    return rooms

