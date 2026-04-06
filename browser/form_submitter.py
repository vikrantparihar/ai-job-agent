class FormSubmitter:

    def find_and_click_submit(self, page):
        selectors = [
            "button[type='submit']",
            "input[type='submit']",
            "button:has-text('Submit')",
            "button:has-text('Apply')",
            "button:has-text('Send')",
            "button:has-text('Next')"
        ]

        for sel in selectors:
            try:
                el = page.query_selector(sel)
                if el:
                    el.click()
                    print(f"🚀 Clicked submit button: {sel}")
                    return True
            except:
                continue

        print("⚠️ Submit button not found")
        return False