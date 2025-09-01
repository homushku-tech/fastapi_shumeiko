from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter
from app.hotels.dao import HotelsDAO
from app.hotels.schemas import HotelSearchArgs, SHotelInfo


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)

@router.get("/{location}")
@cache(expire=20)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
)-> list[SHotelInfo]:
    hotels = await HotelsDAO.find_all(location, date_from, date_to)
    return hotels

@router.post("")
async def post_hotels(
    hotel_data: HotelSearchArgs = Depends()  
):
    new_hotel = await HotelsDAO.add(**hotel_data.__dict__)
    return new_hotel
