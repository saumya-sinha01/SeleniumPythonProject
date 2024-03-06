from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com/")
time.sleep(3)
'''movetoelement'''
login_element=driver.find_element(By.XPATH,'//div[contains(text(),"Login")]').click()
action_chain=ActionChains(driver)
action_chain.move_to_element(login_element).perform()
time.sleep(3)

