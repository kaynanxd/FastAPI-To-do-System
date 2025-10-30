import asyncio
import sys
from http import HTTPStatus

from fastapi import FastAPI

from backend.routers import auth, todos, users
from backend.schemas import Message

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

app.include_router(users.router)
app.include_router(todos.router)
app.include_router(auth.router)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}
