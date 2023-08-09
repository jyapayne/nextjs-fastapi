from fastapi import FastAPI

from api.db.engine import engine

app = FastAPI()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}
