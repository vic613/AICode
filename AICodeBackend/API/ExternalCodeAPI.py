from fastapi import APIRouter,BackgroundTasks
from Models.ExternalCodeModel import ExternalCodeModel
from Services.CodeService import reviewpost
import requests
import json
from Server.Common.Settings import OllamaAPI

externalcodeapi = APIRouter()
urls = [OllamaAPI.url]
headers = {
    "Content-Type": "application/json"
      }

@externalcodeapi.post("/externalcodeapi/externalcodereview")
def codereview(item: ExternalCodeModel):
    llms_name =  item.model,
    if llms_name[0] == "llama3.1":
        url = urls[0]
        payload = {
            "model": "llama3.1",
            "prompt": item.prompt,
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return {"data": response.text}
        else:
            print("error:", response.status_code, response.text)
            return {"item_name": item.model, "error": response.status_code, "data": response.text}
    return {"item_name": item.model, "llms_name": llms_name}