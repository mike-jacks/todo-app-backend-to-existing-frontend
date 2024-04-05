from uuid import UUID

from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: UUID | None = Field(default=None, primary_key=True)
    item: str
    description: str | None = Field(default=None)

class CreateTodoRequest(SQLModel):
    item: str
    description: str
    
class UpdateTodoRequest(SQLModel):
    item: str
    description: str

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
