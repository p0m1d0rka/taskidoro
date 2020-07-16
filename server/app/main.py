from fastapi import FastAPI
from .routes import healthcheck, tasks
app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}