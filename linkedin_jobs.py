from playwright.sync_api import sync_playwright
import time


def apply_linkedin_job(url):
    print("🔥 LINKEDIN BOT STARTED")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            print(f"🌐 Opening: {url}")
            page.goto(url, timeout=60000)

            time.sleep(5)

            # 👉 Try clicking Easy Apply
            try:
                page.click("button:has-text('Easy Apply')", timeout=5000)
                print("✅ Clicked Easy Apply")
            except:
                print("⚠️ Easy Apply not found (still OK)")

            time.sleep(5)

            browser.close()

        return True

    except Exception as e:
        print("❌ Error:", str(e))
        return False