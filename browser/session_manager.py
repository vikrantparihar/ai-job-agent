from playwright.sync_api import sync_playwright

class SessionManager:

    def start(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def close(self):
        try:
            self.context.close()
            self.browser.close()
            self.playwright.stop()
        except:
            pass