from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="RestAPI con FastAPI y MongoDB",
    description="esto es una rest api simple",
    version="0.02",
    openapi_tags=tags_metadata
)

app.include_router(user)

