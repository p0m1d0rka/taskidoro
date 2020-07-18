from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskModelBase(BaseModel):
    title: str
    author: str
    text: Optional[str] = None
    created_at: datetime


class TaskModelIn(TaskModelBase):
    pass


class TaskModelOut(TaskModelBase):
    _id: str