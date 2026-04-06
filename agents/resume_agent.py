def generate_resume(job_desc, profile):
    print("⚡ Using mock LLM (no API call)")

    return f"""
    === GENERATED RESUME ===

    Candidate Profile:
    {profile}

    Tailored for Job:
    {job_desc}

    Skills:
    - Python
    - Machine Learning
    - APIs
    - AI Systems

    Experience:
    3+ years building backend and AI systems
    """