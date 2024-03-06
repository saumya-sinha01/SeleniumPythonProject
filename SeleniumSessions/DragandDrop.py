from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/droppable")
time.sleep(4)

source=driver.find_element(By.XPATH,"//div[@id='draggable']")
target=driver.find_element(By.XPATH,"//div[@id='droppable'")
time.sleep(2)
dragndrop(source,target,driver)
def dragndrop(Src,tar,driver):
    try:

        act_chains=ActionChains(driver)
        #single action drag n drop
        act_chains.drag_and_drop(src, tar).perform()
    except Exception as e:
        print(e)

#multiple action
#act_chains.click_and_hold(source).move_to_element(target).release().perform()