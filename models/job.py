from sqlalchemy import Column, Integer, String
from db.database import Base  # 🔥 IMPORTANT FIX

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    status = Column(String, default="pending")

    # Retry system
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    failure_reason = Column(String, nullable=True)