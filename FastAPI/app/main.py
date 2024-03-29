from typing import List
from fastapi import APIRouter, Body, Depends, FastAPI
from database.models import Company
from database.schemas import CompanyCreate
from database.schemas import RecruitmentList
from database.schemas import RecruitmentCreate
from database import models
from database.models import Users, Recruitment
from database.conn import engine, Session

app = FastAPI()
router = APIRouter()
session = Session()

models.Base.metadata.create_all(bind=engine)
app.include_router(
    router,
    prefix="/recruitment",
    tags=["recruitment"]    
)

@app.post("/create", response_model=RecruitmentCreate)
async def create_recruitment(recruitment_data: RecruitmentCreate = Body(...)):
    data = Recruitment.create(session=session, **recruitment_data.dict())
    return data

@app.post("/modify", response_model=RecruitmentCreate)
async def modify_recruitment(recruitment_data: RecruitmentCreate = Body(...)):
    data = Recruitment.modify(session=session, **recruitment_data.dict())
    return data

@app.post("/delete", response_model=str)
async def delete_recruitment(company_id: str):
    data = Recruitment.delete(session=session, company_id=company_id)
    return data

@app.get("/index", response_model=List[RecruitmentList])
async def get_recruitment_list():
    data = Recruitment.get(session=session)
    return data

@app.post("/company")
def create_company(company_data: CompanyCreate = Body(...)):
    data = Company.create(session=session, **company_data.dict())
    return data

# @app.post("/create")
# def create_user():
#     user = Users(id=2, name="user_test")
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user

