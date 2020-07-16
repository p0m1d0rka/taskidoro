import motor.motor_asyncio
import os
MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_INNER_PORT = int(os.environ["MONGO_INNER_PORT"])
MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_HOST, MONGO_INNER_PORT)

db_instance = client[MONGO_DB_NAME]