print("🔥 NEW AGENT MAIN RUNNING")

from services.job_service import get_next_job, update_job_status
from services.ats_detector import detect_ats
from services.field_resolver import resolve_field
from services.hitl import ask_user
from automation.run_automation import run_automation
from utils.llm import generate_cover_letter


def process_job():
    job = get_next_job()

    if not job:
        print("✅ No jobs left")
        return False

    job_id = job.id
    job_url = job.url

    update_job_status(job_id, "processing")

    print(f"\n🚀 Processing Job: {job_url}")

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
                update_job_status(job_id, "backlog")
                return True

        answers[q] = ans

    # Cover Letter
    cover_letter = generate_cover_letter("Software Engineer Job")
    answers["cover_letter"] = cover_letter

    ats = detect_ats(job_url)

    print(f"🤖 Running automation for {ats}")

    success = run_automation(job_url, answers)

    if success:
        update_job_status(job_id, "applied")
        print("🎉 Applied Successfully!")
    else:
        update_job_status(job_id, "failed")
        print("❌ Failed")

    return True


if __name__ == "__main__":
    while True:
        try:
            has_job = process_job()
            if not has_job:
                break
        except Exception as e:
            print("❌ Error:", e)
            break