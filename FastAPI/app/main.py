from dataclasses import asdict
from typing import Union
from app.database.conn import db

from fastapi import FastAPI
import uvicorn

from FastAPI.app.common.config import conf

def create_app():

    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)


    # app.include_router(index.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)