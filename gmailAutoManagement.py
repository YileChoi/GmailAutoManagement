from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

#Loading Chrome with login Profile
profile_path = "C:\\Users\\Yile Choi\\AppData\\Local\\Google\\Chrome\\User Data"
profile_directory = "Profile 2"

#Chrome Opening up automatically with logged in profiles
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument(f"--profile-directory={profile_directory}")

#Setting up basic selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)

try:
    # Navigating to Gmail
    url = "https://mail.google.com"
    driver.get(url)
    
    # Wait for Gmail to load
    wait = WebDriverWait(driver, 20)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # Search for emails from a specific sender
    sender_email = "noreply@discord.com"  # Write the sender you want to delete email from
    search_box.send_keys(f'from:{sender_email}')
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "UI")))

    # Wait for the checkboxes to be present
    email_checkboxes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "T-Jo-auh")))

    checkbox = driver.find_element(By.XPATH, "//div[@role='checkbox']")
    # checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()

except TimeoutException as e:
    print(f"Timeout waiting for element: {e}")

finally:
    # Close the browser
    # time.sleep(10)
    driver.quit()

# time.sleep(3)
# driver.quit()