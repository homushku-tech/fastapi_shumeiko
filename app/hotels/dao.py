from datetime import date
from sqlalchemy import insert
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
