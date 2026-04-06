import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_cover_letter(job_desc, user_profile):
    prompt = f"""
    Write a short cover letter.

    Job:
    {job_desc}

    Candidate:
    {user_profile}
    """

    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content