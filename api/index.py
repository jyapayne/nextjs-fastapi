from dotenv import dotenv_values
from fastapi import FastAPI

from api.db.engine import engine

config = dotenv_values(".env")

app = FastAPI(root_path="/api")


@app.get("/v1/python")
def hello_world():
    return {"message": "Hello World"}
