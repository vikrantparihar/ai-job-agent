from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    resume_path = Column(String)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    company = Column(String)
    title = Column(String)
    ats_platform = Column(String)
    status = Column(String, default="pending")
    failure_reason = Column(Text)
    unanswered_fields = Column(Text)


class CustomAnswer(Base):
    __tablename__ = "custom_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(Text)
    answer = Column(Text)

    user = relationship("User")