import logging

from fastapi import APIRouter

router = APIRouter(tags=["index"])

@router.get(
    "/",
    responses={200: {"description": "ok"}}
)
async def index() -> dict:
    return {"It's good to see you"}