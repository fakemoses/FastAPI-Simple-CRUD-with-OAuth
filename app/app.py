from fastapi import FastAPI, Depends
from auth.auth_bearer import JWTBearer
from routes.todo_routes import router as todoRouter
from routes.user_routes import router as userRouter

app = FastAPI()

app.include_router(userRouter, tags=["user"], prefix="/user")
app.include_router(todoRouter, dependencies=[Depends(JWTBearer())], tags=["todo"], prefix="/todo")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app!"}
