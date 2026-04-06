import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ====== CHANGE THIS PATH TO YOUR CHROMEDRIVER ======
CHROMEDRIVER_PATH = "/Users/vikrantparihar/Downloads/chromedriver"

# LinkedIn job search URL
JOB_URL = "https://www.linkedin.com/jobs/search/?keywords=AI%20Developer&f_E=2"  # Easy Apply only

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(JOB_URL)
input("⏳ Please login manually in the opened browser... Login complete? Press Enter to continue...")

sleep(3)

# Scroll to load jobs
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

# Find all job cards
job_cards = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search-results__list li")

jobs = []
for card in job_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "h3").text
        company = card.find_element(By.CSS_SELECTOR, "h4").text
        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
        jobs.append({
            "title": title,
            "company": company,
            "link": link
        })
    except:
        continue

with open("job_queue.json", "w") as f:
    json.dump(jobs, f, indent=4)

print(f"🔢 Found job cards: {len(jobs)}")
print(f"✅ Saved {len(jobs)} Easy Apply jobs to job_queue.json")

driver.quit()