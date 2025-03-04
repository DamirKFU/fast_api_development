import pydantic


class RegisterUserRequest(pydantic.BaseModel):
    username: str
