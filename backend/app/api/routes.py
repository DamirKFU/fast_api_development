import fastapi


router = fastapi.APIRouter(prefix="/test", tags=["base"])


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
