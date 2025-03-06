import typing

import fastapi
import sqlmodel

from app.api.users.models import User
from app.api.users.schemas.responce import UserResponse
from app.core.db import SessionDep

router = fastapi.APIRouter(prefix="/test", tags=["base"])


@router.get("/", response_model=list[UserResponse])
async def root(session: SessionDep) -> typing.Any:
    return session.exec(sqlmodel.select(User.id, User.username)).fetchall()
