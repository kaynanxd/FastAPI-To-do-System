from datetime import datetime, timedelta
from http import HTTPStatus
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from pwdlib import PasswordHash
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_session
from backend.models import User
from backend.settings import Settings

settings = Settings()
pwd_context = PasswordHash.recommended()
OAuth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/token", refreshUrl="auth/refresh"
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def get_current_user(
        session: AsyncSession = Depends(get_session),
        token: str = Depends(OAuth2_scheme),
):
    credential_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        subject_email = payload.get("sub")

        if not subject_email:
            raise credential_exception

    except JWTError:
            raise credential_exception

    user = await session.scalar(
        Select(User).where(User.email == subject_email)
    )

    if not user:
        raise credential_exception

    return user
