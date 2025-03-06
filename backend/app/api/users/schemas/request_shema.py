import pydantic
import sqlmodel


class RegisterUserRequest(pydantic.BaseModel):
    username: str
    password: str
    email: pydantic.EmailStr = sqlmodel.Field(max_length=255)
