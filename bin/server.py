import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.app_container import ApplicationContainer
from src.router import api_router
from src.settings import settings

@asynccontextmanager
async def lifespan(_app: FastAPI):
    container = ApplicationContainer()
    os.environ["JOB_NAME"] = "app_server"
    await container.init_resources()  # type: ignore[misc]
    yield
    await container.shutdown_resources()  # type: ignore[misc]

app = FastAPI(
    # lifespan=lifespan,
    docs_url="/api/docs/",
    openapi_url="/api/openapi.json1",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")

def run_app():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=1337,
        log_level=settings.log_level,
        reload=settings.server.reload,
    )


if __name__ == "__main__":
    run_app()
