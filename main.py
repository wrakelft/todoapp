from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import requests as rq

class AddTask(BaseModel):
  tg_id: int
  text: str


class CompleteTask(BaseModel):
  id: int

@asynccontextmanager
async def lifespan(app: FastAPI):
  await init_db()
  print('Bot is ready')
  yield


app = FastAPI(title="ToDo App", lifespan=lifespan)


app.add_middleware(
  CORSMiddleware, #security
  allow_origins=['*'], #url с которых разрешаем запросы
  allow_credentials=True,
  allow_methods=["*"], #какие методы Post Get и тд
  allow_headers=["*"], #Какие headers мб с токенами
)


@app.get("/api/tasks/{tg_id}")
async def tasks(tg_id: int):
  user = await rq.add_user(tg_id)
  return await rq.get_tasks(user.id)


@app.get("/api/main/{tg_id}")
async def profile(tg_id: int):
  user = await rq.add_user(tg_id)
  completed_tasks_count = await rq.get_completed_tasks_count(user.id)
  return {'completedTasks': completed_tasks_count}


@app.post("/api/add")
async def add_task(task: AddTask):
  user = await rq.add_user(task.tg_id)
  await rq.add_task(user.id, task.text)
  return {'status': 'ok'}


@app.patch("/api/completed")
async def complete_task(task: CompleteTask):
  await rq.update_task(task.id)
  return {'status': 'ok'}
