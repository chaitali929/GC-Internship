from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in PATH

try:
    # Open Google
    driver.get("https://www.google.com")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")
    search_query = "Selenium Python"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(2)

    # Extract search result titles
    results = driver.find_elements(By.XPATH, "//h3")
    print("Google Search Results:")
    for idx, result in enumerate(results[:10], start=1):
        print(f"{idx}. {result.text}")

finally:
    # Close the browser
    driver.quit()
