def is_relevant(title):
    keywords = ["AI", "Machine Learning", "Data", "Python", "Deep Learning"]

    for k in keywords:
        if k.lower() in title.lower():
            return True

    return False