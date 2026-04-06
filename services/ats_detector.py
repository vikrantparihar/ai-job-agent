def detect_ats(url):
    if "workday" in url:
        return "workday"
    elif "greenhouse" in url:
        return "greenhouse"
    elif "lever" in url:
        return "lever"
    elif "linkedin" in url:
        return "linkedin"
    return "unknown"