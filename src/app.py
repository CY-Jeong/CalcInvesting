import logging

from fastapi import FastAPI, Security

from src.router.index_router import router as index_router
from src.router.health_router import router as health_router

app = FastAPI(
    title="Calculate Invest",
    description="calculate how much you could make money in specific condition",
    version="0.0.1",
    openapi_url=""
)

app.include_router(
    index_router,
    prefix="/"
)

app.include_router(
    health_router,
    prefix="/"
)

app.include_router(
    
)
