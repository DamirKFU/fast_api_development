import fastapi

import app.api
import app.core.config


def custom_generate_unique_id(route: fastapi.routing.APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


asgi_app: fastapi.FastAPI = fastapi.FastAPI(
    title=app.core.config.settings.PROJECT_NAME,
    openapi_url=f"{app.core.config.settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


asgi_app.include_router(
    app.api.api_router,
    prefix=app.core.config.settings.API_V1_STR,
)
