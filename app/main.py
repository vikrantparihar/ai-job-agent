from db.database import init_db
from services.job_service import add_job
from app.worker import run_worker

if __name__ == "__main__":
    print("🚀 Starting AI Job Agent (Production)")

    init_db()

    # sample jobs
    add_job("Software Engineer", "Python Backend Role")
    add_job("AI Engineer", "LLM + Automation Role")

    run_worker()