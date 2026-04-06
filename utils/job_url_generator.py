import random
import re

def generate_job_urls(keyword, count=3):
    if not keyword:
        raise ValueError("Keyword required")

    slug = re.sub(r'[^a-zA-Z0-9]+', '-', keyword.lower()).strip('-')

    base_url = "https://job-boards.eu.greenhouse.io/test-company/jobs"

    urls = []

    for i in range(count):
        job_id = random.randint(1000, 9999)
        urls.append(f"{base_url}/{slug}-{job_id}")

    return urls