from pydantic import BaseModel

class ExternalCodeModel(BaseModel):
    model: str
    prompt: str

