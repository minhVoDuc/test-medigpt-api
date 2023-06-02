from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os
from model.msg import GptMsg
import gpt_interact as gpt

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World!"}

@app.get("/ping")
def ping():
    return {"msg": "Good!"}

@app.get("/trial/chat")
def trial_chat(msg: str):
    reponse = gpt.get_response(msg)
    return reponse

if __name__ == '__main__':
    # initialize
    ## load env var from .env
    load_dotenv()
    # port = int(os.getenv('PORT'))
    port=8001
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")