from datetime import date
from app.tasks.tasks import send_booking_confirmation_email
from fastapi import APIRouter, Depends, status
from app.bookings.dao import BookingsDAO
from app.bookings.models import Bookings
from app.bookings.schemas import SBooking, SNewBooking
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import RoomFullyBooked

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingsDAO.find_all(user_id = user.id)

@router.post("", status_code=201)
async def add_bookings(
    booking: SNewBooking,
    user: Users = Depends(get_current_user)
    ):
    
    booking = await BookingsDAO.add(user.id, booking.room_id, booking.date_from, booking.date_to)

    if not booking:
        raise RoomFullyBooked
    
    booking_dict =  SNewBooking.model_validate(booking).model_dump()
    
    send_booking_confirmation_email.delay(booking_dict, user.email) #celery task
    return booking_dict

@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user)
):
    await BookingsDAO.delete(id=booking_id, user_id=current_user.id)