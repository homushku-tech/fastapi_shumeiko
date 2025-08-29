from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)