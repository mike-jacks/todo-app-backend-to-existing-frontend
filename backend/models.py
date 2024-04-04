from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item: str

class UpdateTodoRequest(SQLModel):
    item: str

class GetTodosResponse(SQLModel):
    data: list[Todo]

class PostTodosResponse(SQLModel):
    data: Todo
    description: str

class PutTodosResponse(SQLModel):
    data: Todo
    description: str    

class DeleteTodosResponse(SQLModel):
    data: Todo
    description: str
