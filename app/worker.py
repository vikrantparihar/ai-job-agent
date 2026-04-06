import time
from services.job_service import get_next_job, update_status
from app.automation.playwright_apply import apply_to_job

print("🚀 AI Job Worker Started (AUTONOMOUS MODE)")

while True:
    job = get_next_job()

    if job:
        job_id, title, description = job

        print("\n==============================")
        print(f"📌 New Job Found: {title}")
        print("==============================")

        try:
            print("⚙️ Running Playwright automation...")

            success = apply_to_job(title, description)

            if success:
                update_status(job_id, "done")
                print("✅ Job completed successfully")
            else:
                update_status(job_id, "failed")
                print("❌ Job failed")

        except Exception as e:
            update_status(job_id, "failed")
            print("❌ Error:", str(e))

    else:
        print("📭 No jobs in queue...")

    time.sleep(5)