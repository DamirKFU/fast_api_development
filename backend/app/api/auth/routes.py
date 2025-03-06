import fastapi

from app.api.users.models import User
from backend.app.api.users.schemas.request_shema import RegisterUserRequest
from backend.app.api.users.schemas.responce_shema import UserResponse
from app.api.users.utils import get_password_hash
from app.core.db import SessionDep


router = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
async def register(
    request: RegisterUserRequest,
    session: SessionDep,
) -> User:
    user = User(
        email=request.email,
        username=request.username,
        hashed_password=get_password_hash(request.password),
    )
    session.add(user)
    session.commit()
    return user
