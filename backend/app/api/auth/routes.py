import fastapi

from app.api.users.models import User
from app.api.users.schemas.request import RegisterUserRequest
from app.api.users.schemas.responce import UserResponse
from app.core.db import SessionDep


router = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
async def register(
    request: RegisterUserRequest,
    session: SessionDep,
) -> User:
    user = User(username=request.username)
    session.add(user)
    session.commit()
    return user
