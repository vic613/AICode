from pydantic import BaseModel

class LoginModel(BaseModel):
    username: str = None
    password: str = None




