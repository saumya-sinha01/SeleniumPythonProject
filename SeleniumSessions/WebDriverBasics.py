import time

from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)
driver.find_element(By.NAME,'q').send_keys(("Saumya Sinha"))
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="ERWdKc"]/div[1]/span').click()
print(driver.title)
time.sleep(5)
driver.quit()