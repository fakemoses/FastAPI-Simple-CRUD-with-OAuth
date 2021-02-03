from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

# perform all the db actions
from app.db import (
    add_todo,
    delete_todo,
    update_todo,
    retrieve_todo,
    get_todo_list
)
# data models are defined here
from models.models import (
    ResponseModel,
    ErrorResponseModel,
    TodoSchema,
    UpdateTodoModel
)

router = APIRouter()


# create
@router.post("/", response_description="Todo data added into the database")
async def add_todo_data(todo: TodoSchema = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = await add_todo(todo)
    return ResponseModel(new_todo, "todo added successfully.")


# read / get
@router.get("/", response_description="Todo retrieved")
# check if exists
async def get_todoList():
    todo = await get_todo_list()
    if todo:
        return ResponseModel(todo, "Todo data retrieved successfully")
    return ResponseModel(todo, "Empty list returned")

# get the data
@router.get("/{id}", response_description="Todo data retrieved")
async def get_todoList_data(id):
    todo = await retrieve_todo(id)
    if todo:
        return ResponseModel(todo, "Todo data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Todo doesn't exist.")


# update
@router.put("/{id}")
async def update_todo_data(id: str, req: UpdateTodoModel = Body(...)):
    # way to remove keys in dictionary with None values in Python
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_list = await update_todo(id, req)
    if updated_list:
        return ResponseModel(
            "Todo with ID: {} name update is successful".format(id),
            "Todo updated successfully",
        )
    return ErrorResponseModel("An error occurred", 404, "There was an error updating the data.")


@router.delete("/{id}", response_description="Todo data deleted from the database")
async def delete_data(id: str):
    deleted_list = await delete_todo(id)
    if deleted_list:
        return ResponseModel(
            "Todo with ID: {} removed".format(id), "Todo deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )
