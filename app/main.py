import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello"


if __name__ == "__main__":
    uvicorn.run("main:app")
