import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.reddit.com/')
cookies=driver.get_cookies()
print(driver.get_cookies())
#driver.add_cookie({"domain":"saumya.com"})
for cook in cookies:
    print(cook)
    