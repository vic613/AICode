
import uvicorn
from fastapi import FastAPI,BackgroundTasks
from fastapi.responses import RedirectResponse
from pydantic_settings import BaseSettings
from API.CodeAPI import codeapi
from API.LoginAPI import loginapi
from API.ExternalCodeAPI import externalcodeapi
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str ="test@email.com"
    items_per_user: int = 50

settings = Settings()
app = FastAPI()
app.include_router(loginapi)
app.include_router(codeapi)
app.include_router(externalcodeapi)

#swagger = Swagger(app)
@app.get("/")
async def root():
    return RedirectResponse(url='/docs')

#@app.post("/info/{id}")
#async def info():
#    return {
#        "app_name": settings.app_name,
#        "admin_email": settings.admin_email,
#        "items_per_user": settings.items_per_user,
#    }

#@app.post("/upload/{filename}")
#async def upload_and_process(filename: str, background_tasks: BackgroundTasks):
#    background_tasks.add_task(process_file, filename)
#    return {"message": "processing file"}

#def process_file(filename: str):
#    # process file :: takes minimum 3 secs (just an example)
#    pass


if __name__ == "__main__":
    uvicorn.run("main:app")