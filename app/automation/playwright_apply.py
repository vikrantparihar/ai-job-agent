from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def apply_to_job(job_title: str, description: str):
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=50
        )

        context = browser.new_context()
        page = context.new_page()

        try:
            # =========================
            # STEP 1: OPEN GOOGLE
            # =========================
            page.goto(
                "https://www.google.com",
                wait_until="domcontentloaded",
                timeout=30000
            )

            # =========================
            # STEP 2: HANDLE COOKIE POPUP (if any)
            # =========================
            try:
                page.click("button:has-text('Accept all')", timeout=3000)
            except:
                pass

            # =========================
            # STEP 3: WAIT FOR SEARCH BOX
            # =========================
            page.wait_for_selector("input[name='q']", timeout=10000)

            # =========================
            # STEP 4: SEARCH JOB
            # =========================
            search_query = f"{job_title} jobs"

            page.fill("input[name='q']", search_query)
            page.keyboard.press("Enter")

            # =========================
            # STEP 5: WAIT RESULTS
            # =========================
            page.wait_for_timeout(4000)

            print(f"🤖 Search completed for: {job_title}")

            return True

        except PlaywrightTimeoutError as e:
            print("❌ Timeout Error:", str(e))
            return False

        except Exception as e:
            print("❌ Unexpected Error:", str(e))
            return False

        finally:
            browser.close()