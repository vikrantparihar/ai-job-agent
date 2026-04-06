from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome driver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google and print title
driver.get("https://www.google.com")
print("Title:", driver.title)

# Close browser
driver.quit()
