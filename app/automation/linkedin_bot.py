from playwright.sync_api import sync_playwright
import time


SESSION_DIR = "linkedin_profile"


def auto_apply(job_title, max_apply=3):
    with sync_playwright() as p:

        context = p.chromium.launch_persistent_context(
            user_data_dir=SESSION_DIR,
            headless=False
        )

        page = context.new_page()

        # =========================
        # STEP 1 — OPEN JOBS PAGE
        # =========================
        page.goto("https://www.linkedin.com/jobs/")
        page.wait_for_timeout(5000)

        # =========================
        # CHECK LOGIN
        # =========================
        if "checkpoint" in page.url:
            print("❌ CAPTCHA detected")
            input("Solve CAPTCHA and press ENTER...")

        # =========================
        # STEP 2 — SEARCH JOB
        # =========================
        search_box = page.locator("input[aria-label*='Search']")
        search_box.fill(job_title)
        page.keyboard.press("Enter")

        page.wait_for_timeout(5000)

        print(f"🔎 Searching jobs for: {job_title}")

        # =========================
        # STEP 3 — GET JOB CARDS
        # =========================
        job_cards = page.locator("ul li").all()

        applied = 0

        # =========================
        # STEP 4 — LOOP JOBS
        # =========================
        for i in range(min(len(job_cards), 20)):

            if applied >= max_apply:
                print("✅ Max apply limit reached")
                break

            try:
                job_cards[i].click()
                page.wait_for_timeout(3000)

                # =========================
                # STEP 5 — CHECK EASY APPLY
                # =========================
                buttons = page.locator("button")

                easy_apply = None

                for j in range(buttons.count()):
                    text = buttons.nth(j).inner_text()

                    if "Easy Apply" in text:
                        easy_apply = buttons.nth(j)
                        break

                if easy_apply:
                    print(f"⚡ Applying to job {i+1}")

                    easy_apply.click()
                    page.wait_for_timeout(3000)

                    # Try submit (simple flow)
                    try:
                        submit = page.locator("button:has-text('Submit application')")
                        if submit.count() > 0:
                            submit.first.click()
                            print("✅ Application submitted")
                        else:
                            print("⚠️ Multi-step apply detected (skipping)")
                    except:
                        print("⚠️ Could not submit")

                    applied += 1

                else:
                    print(f"⏭️ Skipping job {i+1} (No Easy Apply)")

                time.sleep(2)

            except Exception as e:
                print("⚠️ Error on job:", e)

        context.close()