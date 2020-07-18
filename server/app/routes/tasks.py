from fastapi import APIRouter
from ..config.db import db_instance 
from ..models.task_model import TaskModelIn, TaskModelOut
router = APIRouter()

collection = db_instance.task

@router.get("/tasks", tags=["tasks"])
async def find_all_tasks():
    result = await db_instance.test_collection.insert_one({"test": "doc"})
    return {"status": "ok", "result": repr(result)}

@router.get("/task/{_id}")
async def find_one_task(_id: str = None):
    result = await collection.find_one({"_id": _id})
    return result 

@router.post("/task")
async def create_task(task: TaskModelIn):
    try:
        result = await collection.insert_one(dict(task))
        return {"status": "success", "_id": str(result.inserted_id)}
    except Exception as e:
        return {"status": "error", "error": str(e)}
