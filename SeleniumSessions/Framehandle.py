from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/frames")
time.sleep(2)
driver.switch_to.frame(1)
print()
