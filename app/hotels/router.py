import asyncio
from datetime import date
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter
from app.hotels.dao import HotelsDAO
from app.hotels.schemas import HotelSearchArgs, SHotels


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)

@router.get("{location}")
@cache(expire=20)
async def get_hotels():
    await asyncio.sleep(3)
    hotels = await HotelsDAO.find_all()
    hotels_json = TypeAdapter(list[SHotels]).validate_python(hotels)
    return hotels_json

@router.post("")
async def post_hotels(
    hotel_data: HotelSearchArgs = Depends()  
):
    new_hotel = await HotelsDAO.add(**hotel_data.__dict__)
    return new_hotel
