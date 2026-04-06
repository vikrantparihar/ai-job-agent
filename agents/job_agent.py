from services.ats_detector import detect_ats
from services.browser_service import open_browser
from agents.form_agent import fill_form

def process_job(job):
    url = job[1]

    ats = detect_ats(url)
    print(f"ATS: {ats}")

    browser, page = open_browser()

    page.goto(url)

    fill_form(page)

    browser.close()