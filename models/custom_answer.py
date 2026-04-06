from sqlalchemy import Column, Integer, String
from db.database import Base

class CustomAnswer(Base):
    __tablename__ = "custom_answers"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(String)
    answer = Column(String)