from services.form_filler import fill_form
from services.resume_generator import generate_resume
def process_job(job):
    job_url = job["url"]
    user_id = job["user_id"]

    resume_path = generate_resume(job)
    cover_letter = generate_cover_letter(job)

    unanswered = apply_to_job(
        job_url,
        resume_path,
        cover_letter,
        user_id
    )

    return unanswered