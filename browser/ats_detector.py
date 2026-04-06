class ATSDetector:

    def detect(self, url: str, page_text: str):
        url = url.lower()
        text = page_text.lower()

        if "workday" in url or "workday" in text:
            return "workday"

        if "greenhouse" in url:
            return "greenhouse"

        if "lever" in url:
            return "lever"

        if "linkedin" in url:
            return "linkedin"

        return "unknown"