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