from db.db import init_db, add_job
from agents.job_agent import run_agent

if __name__ == "__main__":
    print("🚀 Starting System...")

    init_db()

    add_job("Software Engineer", "Python role")
    add_job("AI Engineer", "LLM role")

    run_agent()
