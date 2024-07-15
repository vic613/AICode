from fastapi import APIRouter,BackgroundTasks
from Models.CodeModel import CodeModel
from Services.CodeService import reviewpost

codeapi = APIRouter()

@codeapi.post("/codeapi/codereview")
async def codereview(codeModel: CodeModel, background_tasks: BackgroundTasks):
    
   await reviewpost(codeModel)
    #background_tasks.add_task(reviewpost, codeModel)
   return {"message": "processing file"}