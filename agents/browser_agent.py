from playwright.async_api import async_playwright
import asyncio


async def open_and_fill(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print(f"🌐 Opening: {url}")
        await page.goto(url)

        try:
            await page.fill("input[type='text']", "Vikrant Singh")
        except:
            pass

        try:
            await page.fill("input[type='email']", "vikrant@email.com")
        except:
            pass

        print("✅ Attempted form fill")

        await page.wait_for_timeout(5000)
        