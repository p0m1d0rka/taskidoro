from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck", tags=["healthcheck"])
async def healthcheck():
    return {"status": "ok"}
