from selenium import webdriver
from time import sleep

    # Now you can use sleep directly

from selenium.webdriver.common.by import By

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.google.com")
sleep(3)

# Find the search box by its 'name' attribute using the new method
search_box = driver.find_element(By.NAME, "q")

# Interact with the element
search_box.send_keys("Selenium")
sleep(3)
driver.get("https://www.selenium.dev")



search_box.submit()

# Close the browser
driver.quit()