from fastapi import FastAPI
from .user import users


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "MVC fastapi"}



app.mount("/user", users)
