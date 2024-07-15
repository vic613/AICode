from fastapi import APIRouter,BackgroundTasks
from fastapi import FastAPI,BackgroundTasks
from Models.LoginModel import LoginModel
from Services.LoginService import loginpost


loginapi = APIRouter()

@loginapi.post("/loginapi/login")
async def login(loginModel: LoginModel, background_tasks: BackgroundTasks):
    try:
        await loginpost(loginModel)
        # background_tasks.add_task(loginpost, loginModel)
        return {"message": "processing file"}

    except Exception as e:
       print(e)
