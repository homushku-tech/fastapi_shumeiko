from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt
from app.config import settings
from app.users.dao import UsersDAO

def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=401)
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise HTTPException
    expire: str = payload.get("exp")
    if  (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException
    user = await UsersDAO.find_id(int(user_id))
    if not user:
        raise HTTPException
    
    return user