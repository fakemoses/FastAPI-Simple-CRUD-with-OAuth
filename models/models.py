from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "contact@me.my",
                "password": "weakpassword"
            }
        }


class TodoSchema(BaseModel):
    task: str = Field(...)
    createdBy: str = Field(...)
    dateCreated: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "task": "Example Task",
                "createdBy": "Moses",
                "dateCreated": "01-02-2021",
            }
        }


class UpdateTodoModel(BaseModel):
    task: Optional[str]
    createdBy: Optional[str]
    dateCreated: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "task": "Example Task",
                "createdBy": "Moses",
                "dateCreated": "01-02-2021",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
