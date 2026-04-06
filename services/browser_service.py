from playwright.sync_api import sync_playwright

def open_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    return browser, page