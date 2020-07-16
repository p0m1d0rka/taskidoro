from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    title: str
    author: str
    text: Optional[str] = None
    created_at: datetime