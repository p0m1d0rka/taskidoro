from fastapi import APIRouter
from ..config.db import db_instance 
from ..models.task import Task
router = APIRouter()

@router.get("/tasks", tags=["tasks"])
async def tasks():
    result = await db_instance.test_collection.insert_one({"test": "doc"})
    return {"status": "ok", "result": repr(result)}
