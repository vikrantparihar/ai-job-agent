from playwright.sync_api import sync_playwright
import time
import random
from logger import log_info, log_error
from db.database import save_job
from ai.cover_letter import generate_cover_letter


# -------------------------
# SAFE CLICK
# -------------------------
def safe_click(locator, retries=3):
    for i in range(retries):
        try:
            locator.first.click(timeout=5000, force=True)
            return True
        except Exception as e:
            log_error(f"Click retry {i+1}: {e}")
            time.sleep(2)
    return False


# -------------------------
# EASY APPLY HANDLER
# -------------------------
def handle_easy_apply(page, job_title):
    try:
        log_info("🧠 Filling Easy Apply form...")

        cover_letter = generate_cover_letter(job_title)

        for step in range(6):
            time.sleep(random.randint(2, 4))

            # EMAIL
            email = page.locator("input[type='email']")
            if email.count() > 0:
                email.first.fill("vikrantsinghparihar35@gmail.com")

            # PHONE
            phone = page.locator("input[type='tel']")
            if phone.count() > 0:
                phone.first.fill("9584603250")

            # TEXT INPUTS
            text_inputs = page.locator("input[type='text']")
            for i in range(text_inputs.count()):
                try:
                    inp = text_inputs.nth(i)
                    if inp.input_value() == "":
                        inp.fill("1")
                except:
                    pass

            # COVER LETTER
            textarea = page.locator("textarea")
            if textarea.count() > 0:
                try:
                    textarea.first.fill(cover_letter)
                except:
                    pass

            # YES RADIO
            yes_options = page.locator("label:has-text('Yes')")
            if yes_options.count() > 0:
                safe_click(yes_options.first)

            # DROPDOWNS
            selects = page.locator("select")
            for i in range(selects.count()):
                try:
                    selects.nth(i).select_option(index=1)
                except:
                    pass

            # BUTTON FLOW
            submit = page.locator("button:has-text('Submit')")
            review = page.locator("button:has-text('Review')")
            next_btn = page.locator("button:has-text('Next')")

            if submit.count() > 0:
                safe_click(submit.first)
                log_info("🎉 Application Submitted!")
                return True

            elif review.count() > 0:
                safe_click(review.first)
                continue

            elif next_btn.count() > 0:
                safe_click(next_btn.first)
                continue

            else:
                break

        return False

    except Exception as e:
        log_error(f"Form error: {e}")
        return False


# -------------------------
# LOAD JOBS
# -------------------------
def load_jobs(page):
    log_info("🔄 Loading jobs by scrolling...")

    for _ in range(8):
        page.mouse.wheel(0, 4000)
        time.sleep(2)


# -------------------------
# MAIN FUNCTION
# -------------------------
def auto_apply(keyword="AI Engineer", location="India", limit=3):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        log_info("👉 Opening LinkedIn Jobs...")

        search_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword.replace(' ', '%20')}&location={location.replace(' ', '%20')}"
        page.goto(search_url)

        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(5000)

        # LOGIN CHECK
        if "login" in page.url:
            log_error("❌ Session expired — login again")
            return

        load_jobs(page)

        try:
            page.wait_for_selector("ul.jobs-search__results-list li", timeout=20000)
        except:
            log_error("❌ Jobs not loaded")
            return

        log_info("✅ Jobs loaded")

        applied = 0

        # -------------------------
        # MAIN LOOP (FIXED)
        # -------------------------
        for i in range(15):

            if applied >= limit:
                break

            try:
                jobs = page.locator("ul.jobs-search__results-list li")

                count = jobs.count()
                if i >= count:
                    break

                job = jobs.nth(i)

                # ✅ WAIT INSTEAD OF SCROLL (FIX)
                job.wait_for(state="visible", timeout=5000)

                time.sleep(1)

                if not safe_click(job):
                    continue

                time.sleep(random.randint(2, 4))

                # GET TITLE
                try:
                    title = page.locator("h2").first.inner_text()
                except:
                    title = "AI Engineer"

                easy_btn = page.locator("button.jobs-apply-button")

                if easy_btn.count() > 0:

                    if safe_click(easy_btn.first):
                        time.sleep(3)

                        success = handle_easy_apply(page, title)

                        if success:
                            applied += 1
                            save_job(title, "LinkedIn", "APPLIED")

                        close = page.locator("button[aria-label='Dismiss']")
                        if close.count() > 0:
                            safe_click(close.first)

                else:
                    log_info("⏭ Skipped (No Easy Apply)")

            except Exception as e:
                log_error(f"⚠️ Job error: {e}")
                continue

        log_info(f"🎯 DONE: Applied {applied}")

        context.close()
        browser.close()