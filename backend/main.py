from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from db import engine
from models import Todo

from models import Todo, GetTodosResponse, PostTodosResponse, PutTodosResponse, DeleteTodosResponse, UpdateTodoRequest

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

TODOS = [
    Todo(id=1, item="Teach class"),
    Todo(id=2, item="Taxes!")
]

@app.get("/todo")
async def get_todos() -> GetTodosResponse:
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
    return GetTodosResponse(data=todos)

@app.post("/todo")
async def add_todo(todo: Todo) -> PostTodosResponse:
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
    return PostTodosResponse(data=todo, description=f"{todo.item} has been added.")

@app.put("/todo/{id}")
async def update_todo(id: int, updated_todo: UpdateTodoRequest) -> PutTodosResponse:
    with Session(engine) as session:
        todo = session.exec(select(Todo).where(Todo.id == id)).first()
        if todo is None:
            raise HTTPException(status=404, detail=f"ID {id} not found.")
        todo.item = updated_todo.item
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return PutTodosResponse(data=todo, description=f"{todo.item} has been updated.")

@app.delete("/todo/{id}")
async def delete_todo(id: int) -> DeleteTodosResponse:
    with Session(engine) as session:
        todo = session.exec(select(Todo).where(Todo.id == id)).first()
        if todo is None:
            raise HTTPException(status=404, detail=f"ID {id} not found.")
        item_name = todo.item
        session.delete(todo)
        session.commit()
        return DeleteTodosResponse(data=todo, description=f"{item_name} has been deleted.")


