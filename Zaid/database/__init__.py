import motor.motor_asyncio

from config import DATABASE_URL
cli = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

dbb = cli.program
