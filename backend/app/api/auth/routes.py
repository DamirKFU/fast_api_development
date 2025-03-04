import fastapi


router = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def login(request: fastapi.Request) -> dict[str, str]:
    return {"message": "Hello World"}
