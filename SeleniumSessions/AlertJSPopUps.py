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
driver.get("https://demoqa.com/alerts")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#alertButton').click()
time.sleep(3)
try:
    # Switch to the alert
    alert = driver.switch_to.alert
    time.sleep(3)
    print("Alert Text:", alert.text)
    # Accept the alert (Click OK)
    alert.accept()
    print("i accepted")
except Exception as e:
    print("No alert found or unable to switch to the alert")
#
timealert = driver.find_element(By.CSS_SELECTOR, '#alertButton')



def abc(timealert):
    try:
        # Switch to the alert
        timealert.click()
        alert = driver.switch_to.alert
        time.sleep(5)
        print("Alert Text:", alert.text)
        # Accept the alert (Click OK)
        alert.dismiss()
    except Exception as e:
        print("No alert found or unable to switch to the alert")

abc(timealert)
# Close the browser window
driver.quit()

# # Wait for the input field to be clickable, then send keys
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,'alertButton'))).click()
# # Select '13: 13' from the dropdown
# Select(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
