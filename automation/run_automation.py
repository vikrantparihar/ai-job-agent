from playwright.sync_api import sync_playwright


def map_answer(question, answers):
    q = question.lower()

    if "relocation" in q:
        return answers.get("Are you open to relocation?", "Yes")

    if "salary" in q:
        return answers.get("Expected salary?", "10 LPA")

    if "why" in q:
        return answers.get("Why do you want this job?", "I am passionate about this role.")

    if "cover letter" in q:
        return answers.get("cover_letter", "")

    return "Yes"


def fill_linkedin_form(page, answers):
    print("🧠 Smart Filling Started...")

    while True:
        labels = page.locator("label")

        for i in range(labels.count()):
            try:
                question = labels.nth(i).inner_text()
                answer = map_answer(question, answers)

                inputs = labels.nth(i).locator("xpath=..//input")

                if inputs.count() > 0:
                    inputs.first.fill(answer)
            except:
                pass

        # Resume upload
        file_inputs = page.locator("input[type='file']")
        for i in range(file_inputs.count()):
            try:
                file_inputs.nth(i).set_input_files("resume.pdf")
                print("📄 Resume uploaded")
            except:
                pass

        # Navigation
        if page.locator("button:has-text('Next')").count() > 0:
            page.click("button:has-text('Next')")
            page.wait_for_timeout(2000)

        elif page.locator("button:has-text('Review')").count() > 0:
            page.click("button:has-text('Review')")
            page.wait_for_timeout(2000)

        elif page.locator("button:has-text('Submit')").count() > 0:
            page.click("button:has-text('Submit')")
            return True

        else:
            return False


def fill_workday_form(page, answers):
    print("🏢 Filling Workday form...")

    inputs = page.locator("input")

    for i in range(inputs.count()):
        try:
            inputs.nth(i).fill("Test")
        except:
            pass

    return True


def run_automation(job_url, answers):
    from services.ats_detector import detect_ats

    ats = detect_ats(job_url)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(job_url)

        if ats == "linkedin":
            try:
                page.wait_for_selector("button:has-text('Easy Apply')", timeout=15000)
                page.click("button:has-text('Easy Apply')")
            except:
                print("❌ Easy Apply not found")
                return False

            success = fill_linkedin_form(page, answers)

        elif ats == "workday":
            success = fill_workday_form(page, answers)

        else:
            print("❌ Unsupported ATS")
            success = False

        browser.close()
        return success