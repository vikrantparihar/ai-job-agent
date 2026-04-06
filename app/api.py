from fastapi import FastAPI
from pydantic import BaseModel

from services.job_service import add_job, get_all_jobs

app = FastAPI()


# =========================
# SCHEMA (IMPORTANT FIX)
# =========================
class JobCreate(BaseModel):
    title: str
    description: str


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def home():
    return {"status": "AI Job Agent Running"}


# =========================
# ADD JOB (FIXED JSON BODY)
# =========================
@app.post("/add-job")
def create_job(job: JobCreate):
    job_id = add_job(job.title, job.description)
    return {
        "message": "Job added successfully",
        "job_id": job_id
    }


# =========================
# GET ALL JOBS
# =========================
@app.get("/jobs")
def list_jobs():
    return get_all_jobs()