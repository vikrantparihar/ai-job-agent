from playwright.sync_api import sync_playwright

class BrowserController:
    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()

    def goto(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def get_page_text(self):
        return self.page.inner_text("body")

    def close(self):
        self.browser.close()
        self.playwright.stop()