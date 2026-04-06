# linkedin_auto_apply.py

from playwright.sync_api import sync_playwright
import time


def apply_linkedin_job(url, answers):
    """
    url: LinkedIn job URL
    answers: dict (question -> answer)
    """

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            print(f"🌐 Opening job: {url}")
            page.goto(url, timeout=60000)

            # 🔐 LOGIN CHECK (assumes already logged in)
            time.sleep(3)

            # 👉 Click Easy Apply
            try:
                page.click("button:has-text('Easy Apply')", timeout=5000)
                print("✅ Clicked Easy Apply")
            except:
                print("❌ Easy Apply button not found")
                browser.close()
                return False

            time.sleep(2)

            # 🔁 Multi-step form handling
            while True:
                time.sleep(2)

                # 🧠 Fill inputs using answers
                inputs = page.locator("input")

                for i in range(inputs.count()):
                    try:
                        input_box = inputs.nth(i)
                        label = input_box.get_attribute("aria-label")

                        if not label:
                            continue

                        for question, answer in answers.items():
                            if question.lower() in label.lower():
                                input_box.fill(answer)
                                print(f"✏️ Filled: {label} → {answer}")

                    except:
                        continue

                # 🔘 Fill dropdowns (basic)
                selects = page.locator("select")

                for i in range(selects.count()):
                    try:
                        select = selects.nth(i)
                        select.select_option(index=1)
                        print("📌 Selected dropdown option")
                    except:
                        continue

                # 👉 Click Next or Submit
                if page.locator("button:has-text('Next')").count() > 0:
                    page.click("button:has-text('Next')")
                    print("➡️ Clicking Next")
                    continue

                elif page.locator("button:has-text('Review')").count() > 0:
                    page.click("button:has-text('Review')")
                    print("👀 Reviewing application")
                    continue

                elif page.locator("button:has-text('Submit')").count() > 0:
                    page.click("button:has-text('Submit')")
                    print("📤 Application Submitted!")
                    break

                else:
                    print("⚠️ No Next/Submit button found")
                    break

            time.sleep(3)
            browser.close()

        return True

    except Exception as e:
        print(f"❌ Error in LinkedIn automation: {str(e)}")
        return False