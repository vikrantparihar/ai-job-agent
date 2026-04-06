import time
from db.database import SessionLocal
from models.job import Job

from browser.runner import JobRunner
from services.retry_manager import RetryManager


def run_job_queue_forever():
    print("🤖 AI JOB AGENT LOOP STARTED")

    runner = JobRunner(headless=False)
    retry = RetryManager()

    while True:
        db = SessionLocal()

        try:
            jobs = db.query(Job).filter(Job.status == "pending").all()

            if not jobs:
                print("🟡 No pending jobs... waiting")
                time.sleep(5)
                continue

            print(f"🚀 Found {len(jobs)} jobs")

            for job in jobs:
                print(f"\n⚙️ Processing Job: {job.title} | {job.url}")

                try:
                    if not job.url:
                        raise Exception("Job URL is missing")

                    # 🔥 STEP 1: mark processing (IMPORTANT)
                    retry.mark_processing(job)
                    db.commit()

                    # 🔥 STEP 2: run automation
                    result = runner.run(
                        job.url,
                        candidate={
                            "name": "Demo Candidate",
                            "skills": "Python, FastAPI, AI",
                            "experience": "3+ years software engineer",
                            "email": "demo@email.com",
                            "phone": "9999999999"
                        }
                    )

                    print("🧠 Result:", result)

                    # 🔥 STEP 3: REAL SUCCESS CHECK
                    if result and result.get("submitted") is True:
                        retry.mark_success(job)
                        job.ats_platform = result.get("ats", "unknown")
                    else:
                        retry.mark_failure(job, "Submission not confirmed")

                except Exception as e:
                    print("❌ Job Failed:", str(e))
                    retry.mark_failure(job, str(e))

                # 💾 ONLY COMMIT (NO db.add)
                db.commit()

        except Exception as e:
            print("❌ Queue Error:", str(e))

        finally:
            db.close()

        time.sleep(5)