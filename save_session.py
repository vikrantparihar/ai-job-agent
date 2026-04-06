from playwright.sync_api import sync_playwright

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.linkedin.com/login")

        print("👉 Manually login karo (email + password + OTP)")
        input("✅ Login hone ke baad ENTER dabao...")

        # Save session
        context.storage_state(path="auth.json")
        print("✅ Session saved (auth.json)")

        browser.close()

if __name__ == "__main__":
    save_session()
