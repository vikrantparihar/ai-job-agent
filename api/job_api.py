from fastapi import FastAPI
from pydantic import BaseModel
from db.db import cursor, conn

app = FastAPI()


class JobRequest(BaseModel):
    url: str
    company: str
    title: str


@app.post("/add-job")
def create_job(job: JobRequest):
    try:
        cursor.execute("""
            INSERT INTO jobs (url, company, title, status)
            VALUES (?, ?, ?, 'pending')
        """, (job.url, job.company, job.title))

        conn.commit()

        print("✅ Job inserted in DB")

        return {"status": "saved in DB"}

    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}