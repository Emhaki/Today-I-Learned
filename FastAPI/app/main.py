from fastapi import Depends, FastAPI
from database.conn import Session
from database import models
from database.models import Users
from database.conn import engine

app = FastAPI()
session = Session()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def index():

    example = session.query(Users).all()

    return example

@app.post("/create")
def create_user():
    user = Users(id=1, name="haki_test")
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
