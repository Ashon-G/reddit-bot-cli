# backend/bots/linkedin_bot.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from database.supabase_client import log_event

def run_linkedin(keyword: str, platform: str):
    # Initialize WebDriver (Chrome in this case)
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Navigate to LinkedIn
    driver.get("https://www.linkedin.com/login")
    
    # Log into LinkedIn
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    
    username.send_keys("your_linkedin_email")
    password.send_keys("your_linkedin_password")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    
    # Search for the keyword
    search_box = driver.find_element_by_xpath("//input[@aria-label='Search']")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    # Simulate connecting or sending a message to users
    time.sleep(2)  # Wait for search results to load
    users = driver.find_elements_by_xpath("//span[text()='Connect']")
    for user in users[:5]:  # Limit to first 5 users to avoid spam
        user.click()
        log_event(platform, "User Name", f"Sent connection request with keyword: {keyword}")
    
    # Close the driver
    driver.quit()
