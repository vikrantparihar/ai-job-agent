print("🔥 NEW AGENT MAIN RUNNING")

from services.job_service import get_next_job, update_job_status
from services.ats_detector import detect_ats
from services.field_resolver import resolve_field
from services.hitl import ask_user
from automation.run_automation import run_automation


def process_job():
    job = get_next_job()

    if not job:
        print("✅ No jobs left")
        return False

    print(f"\n🚀 Processing Job: {job.url}")

    answers = {}

    questions = [
        "Are you open to relocation?",
        "Expected salary?",
        "Why do you want this job?"
    ]

    for q in questions:
        print(f"➡️ {q}")

        ans = resolve_field(q, user_id=1)

        if not ans:
            print("⚠️ Asking user...")
            ans = ask_user(q)

            if not ans:
                print("❌ Moving to backlog")
                update_job_status(job.id, "backlog")
                return True

        print(f"✅ {ans}")
        answers[q] = ans

    ats = detect_ats(job.url)
    job.ats_platform = ats

    print(f"🤖 Running automation for {ats}")

    success = run_automation(job, answers)

    if success:
        update_job_status(job.id, "applied")
        print("🎉 Applied Successfully!")
    else:
        update_job_status(job.id, "failed")
        print("❌ Failed")

    return True


if __name__ == "__main__":
    while True:
        has_job = process_job()
        if not has_job:
            break