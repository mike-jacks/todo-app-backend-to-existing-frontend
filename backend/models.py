from uuid import UUID

from pydantic import BaseModel
from sqlmodel import SQLModel, Field
import sqlmodel

from sqlalchemy import Column, String

class Todo(SQLModel, table=True):
    id: UUID | None = Field(default=None, primary_key=True)
    item: str
    description: str = Field(default="Default", sa_column=Column(server_default="Default", nullable=False, type_=sqlmodel.String))

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
