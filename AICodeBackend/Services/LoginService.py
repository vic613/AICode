import os
from fastapi import HTTPException
import motor.motor_asyncio
from Models.LoginModel import LoginModel
from Server.Common.Settings import DBConnection
    
client = motor.motor_asyncio.AsyncIOMotorClient(DBConnection.connectionstring,DBConnection.portnumber)
db = client.AICode
UserCollection = db["UserCollection"]

async def loginpost(loginModel: LoginModel)->LoginModel:
   
    try:
      
        doc = await UserCollection.find_one({"username": str(loginModel.username), "password":str(loginModel.password)})
        

        if not doc:
            raise HTTPException(status_code=404, detail="Not Found")

        return LoginModel(
            username=doc["username"],
        )
    
    except Exception as e:
       print(e)
   
   
