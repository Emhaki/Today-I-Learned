from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey,
    select,
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
    def get(cls, session):
        stmt = select(Recruitment, Company).join(Company)
        result = session.execute(stmt)
        data = result.fetchall()

        recruitment_list = []
        
        for recruitment, company in data:
            recruitment_list.append({
                "recruitment_id": recruitment.id,
                "company_name": company.name,
                "nation": company.country,
                "region": company.region,
                "recruit_position": recruitment.recruit_position,
                "recruit_reward": recruitment.recruit_reward,
                "use_skill": recruitment.use_skill
            })

        return recruitment_list

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
    
    @classmethod
    def modify(cls, session, company_id, recruit_position, recruit_reward, recruit_content, use_skill):
        
        result = session.execute(
            select(Recruitment)
            .where(Recruitment.company_id == company_id)
        )
        
        data = result.scalar()
        # session.delete(data)
        # session.commit()
        # return data
        if data:
            # 레코드를 찾았을 때만 수정 수행
            data.company_id = company_id
            data.recruit_position = recruit_position
            data.recruit_reward = recruit_reward
            data.recruit_content = recruit_content
            data.use_skill = use_skill

            session.commit()
            return data
        else:
            # 레코드가 없을 경우 None반환
            return None
        
    @classmethod
    def delete(cls, session, company_id):

        result = session.execute(
            select(Recruitment)
            .where(Recruitment.company_id == company_id)
        )

        data = result.scalar()
        if data:
            session.delete(data)
            session.commit()

            return "Success"

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(20), nullable=False)
    region = Column(String(20), nullable=False)

    recruitment = relationship("Recruitment", back_populates="company")
