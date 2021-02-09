import motor.motor_asyncio
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os
import bcrypt

load_dotenv()

MONGO_DETAILS = os.getenv('MONGO_URI')


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

todoDB = client.todo
userDB = client.user

todo_collection = todoDB.get_collection("todo_collection")

user_collection = userDB.get_collection("user_collection")


def todo_parser(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "task": todo["task"],
        "createdBy": todo["createdBy"],
        "dateCreated": todo["dateCreated"],
    }


# Crud Methods for the DB
# Retrieve all todo present in the database
async def get_todo_list():
    #this append needs to be fixed
    todoList = []
    async for todo in todo_collection.find():
        temp = todo_parser(todo)
        todoList.append(temp)
    return todoList

# Add a new todo into to the database
async def add_todo(todo_data: dict) -> dict:
    todo = await todo_collection.insert_one(todo_data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_parser(new_todo)


# Retrieve a todo-list with a matching ID
async def retrieve_todo(id: str) -> dict:
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_parser(todo)


# Update a todo with a matching ID
async def update_todo(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        updated_todo = await todo_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_todo:
            return True
        return False


# Delete a todo from the database
async def delete_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        await todo_collection.delete_one({"_id": ObjectId(id)})
        return True


# USER related DB
async def get_user(email: str, password: str):
    # need to hash the password
    user = await user_collection.find_one({"email": email, "password": password})
    checkPass = await bcrypt.checkpw(password, user.password)
    if user and checkPass:
        return True
    return False
