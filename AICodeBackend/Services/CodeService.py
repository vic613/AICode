import code
import os
from fastapi import HTTPException
import motor.motor_asyncio
from Models.CodeModel import CodeModel
from Server.Common.Settings import DBConnection
from Modules.ModulesTrain.CodeTrain import CodeTrain
    
client = motor.motor_asyncio.AsyncIOMotorClient(DBConnection.connectionstring,DBConnection.portnumber)
db = client.AICode
UserCollection = db["UserCollection"]

async def reviewpost(codeModel: CodeModel)->CodeModel:
   
    try:
      
        # doc = await UserCollection.find_one({"value": str(codeModel.value)})
        

        # if not doc:
        #     raise HTTPException(status_code=404, detail="Not Found")
        CodeTrain.calc()
        return CodeModel(
            value="Success"
        )
    
    except Exception as e:
       print(e)
   
   
