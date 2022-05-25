import logging

from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get(
    "/health",
    responses={200: {"description": "ok"}}
)
async def index() -> dict:
    return {"OK"}