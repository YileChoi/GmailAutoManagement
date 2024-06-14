from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Loading Chrome with login Profile
profile_path = "C:\\Users\\Yile Choi\\AppData\\Local\\Google\\Chrome\\User Data"
profile_directory = "Profile 2"

#Chrome Opening up automatically with logged in profiles
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument(f"--profile-directory={profile_directory}")
# options.add_argument('--no-first-run')
# options.add_argument('--no-default-browser-check')

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)

url = "https://mail.google.com"
driver.get(url)

# input_element = driver.find_element(By.CLASS_NAME, "truncate")
# input_element.send_keys("test" + Keys.ENTER)

# time.sleep(3)
# driver.quit()