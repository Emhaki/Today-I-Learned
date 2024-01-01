from pydantic import BaseModel

class User(BaseModel):
    id: int
    status: str
    email: str
    pw: str
    name: str
    phone_number: str
    profile_img: str
    sns_type: str
    marketing_agree: str

    class Config:
        orm_mode = True

class RecruitmentCreate(BaseModel):
    company_id: int
    recruit_position: str
    recruit_reward: int
    recruit_content: str
    use_skill: str

class RecruitmentList(BaseModel):
    recruitment_id: int
    company_name: str
    country: str
    region: str
    recruit_position: str
    recruit_reward: int
    use_skill: str

class CompanyCreate(BaseModel):
    id: int
    name: str
    country: str
    region: str