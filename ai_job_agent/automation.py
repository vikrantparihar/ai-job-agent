import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def start_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    input("Login manually and press ENTER...")
    return driver

def apply_job(driver):
    try:
        btn = driver.find_element(By.XPATH, "//button[contains(., 'Easy Apply')]")
        btn.click()
        time.sleep(2)

        buttons = driver.find_elements(By.TAG_NAME, "button")
        for b in buttons:
            if "submit" in b.text.lower():
                b.click()

        return True
    except:
        return False