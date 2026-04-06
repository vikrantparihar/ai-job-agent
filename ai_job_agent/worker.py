import time
from db import get_next_job, update_job_status
from linkedin_auto_apply import apply_jobs

def run_worker():
    print("🚀 Worker Started...")

    while True:
        job = get_next_job()

        if not job:
            print("No jobs in queue...")
            time.sleep(5)
            continue

        job_id, title, description = job

        try:
            print(f"\n📌 Working on: {title}")

            update_job_status(job_id, "processing")

            apply_jobs(job)

            update_job_status(job_id, "done")

            print("✅ Completed\n")

        except Exception as e:
            print("❌ Error:", e)
            update_job_status(job_id, "failed")

        time.sleep(3)

if __name__ == "__main__":
    run_worker()