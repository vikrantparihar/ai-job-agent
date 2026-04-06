def apply_to_job(url, resume_path, cover_letter, user_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)

        ats = detect_ats(page, url)

        unanswered = fill_form(
            page,
            ats,
            resume_path,
            cover_letter,
            user_id
        )

        page.click("button[type='submit']")

        browser.close()

        return unanswered