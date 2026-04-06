from fastapi import FastAPI
from pydantic import BaseModel
from db.database import SessionLocal
from models.job import Job

app = FastAPI()

# --------------------
# INPUT FORMAT
# --------------------
class JobRequest(BaseModel):
    title: str

# --------------------
# CREATE JOB API
# --------------------
@app.post("/job")
def create_job(job: JobRequest):
    db = SessionLocal()

    new_job = Job(
        title=job.title,
        status="pending"
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    db.close()

    return {
        "message": "Job created successfully",
        "job_id": new_job.id
    }

# --------------------
# TEST API
# --------------------
@app.get("/")
def home():
    return {"status": "AI Agent Running 🚀"}