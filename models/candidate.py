from sqlalchemy import Column, Integer, String, Text
from db.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String)
    phone = Column(String)

    skills = Column(Text)
    experience = Column(Text)
    education = Column(Text)

    resume_path = Column(String)