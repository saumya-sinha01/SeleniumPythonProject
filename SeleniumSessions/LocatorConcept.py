from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/30-day-free-trial/")
time.sleep(3)
driver.find_element(By.ID,'Form_getForm_Name').send_keys("SaumyaOrange")
driver.find_element(By.ID,'Form_getForm_Email').send_keys("Saumya")
#driver.find_element(By.ID,'Form_getForm_Contact').send_keys("saumya@abc.com")
driver.find_element(By.XPATH,'//*[@id="Form_getForm_Contact"]').send_keys("+14253000000")
element_country=driver.find_element(By.ID,'Form_getForm_Country')
select=Select(element_country)
select.select_by_visible_text('China')
time.sleep(3)
driver.find_element(By.CLASS_NAME,'recaptcha-checkbox-checkmark').click()