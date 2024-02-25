from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/30-day-free-trial/")