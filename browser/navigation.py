import time

class Navigator:

    def click_next(self, page):
        selectors = [
            "button:has-text('Next')",
            "button:has-text('Continue')",
            "button:has-text('Save and Continue')",
            "button[type='button']"
        ]

        for sel in selectors:
            try:
                el = page.query_selector(sel)
                if el:
                    el.click()
                    print(f"➡️ Clicked navigation: {sel}")
                    time.sleep(2)
                    return True
            except:
                continue

        return False