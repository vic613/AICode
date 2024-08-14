from pydantic import BaseModel

class CodeModel(BaseModel):
    prompt: str = None
    resultdata: str = None



