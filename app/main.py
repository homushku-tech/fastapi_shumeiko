from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as bookings_router
from app.users.router import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(bookings_router)



origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],  
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers","Access-Authorization"]

)
# @app.get("/hotels/{hotel_id}")
# def get_hotels(hotel_id: int):
#     return {"message": "Привет, мир"}

# class SHotel(BaseModel):
#     address: str
#     name: str
#     stars: int


# class HotelSearchArgs:
#     def __init__(
#         self,
#         location: str,
#         date_from: date,
#         date_to: date,
#         stars: Optional[int] = Query(None, ge=1, le=5), 
#         has_spa: Optional[bool] = None,        
#     ):
#         self.location = location
#         self.date_from = date_from
#         self.date_to = date_to
#         self.stars = stars
#         self.has_spa = has_spa


# @app.get("/hotels")
# def get_hotels(
#   search_args: HotelSearchArgs = Depends()  
# ):
#     return search_args




# @app.get("/hotels")
# def get_hotels(
#     location: str,
#     date_from: date,
#     date_to: date,
#     stars: Optional[int] = Query(None, ge=1, le=5), 
#     has_spa: Optional[bool] = None,
# ) -> list[SHotel]:
#     hotels = [
#         {
#             "address": "ул. Гагарина, 1, Алтай",
#             "name": "Super Hotel",
#             "stars": 5,
#         }
#     ]

#     return hotels
