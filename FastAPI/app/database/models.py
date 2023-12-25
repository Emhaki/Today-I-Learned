from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
)
from database.conn import Base, Session
from sqlalchemy.orm import relationship



class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum("active", "deleted", "blocked"), default="active")
    email = Column(String(length=255), nullable=True)
    pw = Column(String(length=2000), nullable=True)
    name = Column(String(length=255), nullable=True)
    phone_number = Column(String(length=20), nullable=True, unique=True)
    profile_img = Column(String(length=1000), nullable=True)
    sns_type = Column(Enum("FB", "G", "K"), nullable=True)
    marketing_agree = Column(Boolean, nullable=True, default=True)
    # keys = relationship("ApiKeys", back_populates="users")

class Recruitment(Base):
    __tablename__ = "recruitment"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    recruit_position = Column(String(50), nullable=True)
    recruit_reward = Column(Integer, nullable=True)
    recruit_content = Column(String(200), nullable=True)
    use_skill = Column(String(100), nullable=True)

    company = relationship("Company", back_populates="recruitment")

    @classmethod
    def create(cls, session, company_id, recruit_position, recruit_reward, recruit_content, use_skill):
        recruitment_data = {
            "company_id": company_id,
            "recruit_position": recruit_position,
            "recruit_reward": recruit_reward,
            "recruit_content": recruit_content,
            "use_skill": use_skill,
        }

        new_recruitment = cls(**recruitment_data)
        session.add(new_recruitment)
        session.commit()
        return new_recruitment
    

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(20), nullable=False)
    region = Column(String(20), nullable=False)

    recruitment = relationship("Recruitment", back_populates="company")
