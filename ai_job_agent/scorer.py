def score_job(text):
    keywords = [
        "python", "ai", "machine learning",
        "backend", "data", "fastapi"
    ]

    text = text.lower()
    score = 0

    for k in keywords:
        if k in text:
            score += 10

    return score