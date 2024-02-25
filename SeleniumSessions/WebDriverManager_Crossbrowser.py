import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import  By
from webdriver_manager.firefox import GeckoDriverManager

browserName="chrome"
if browserName =='chrome':
    #driver=webdriver.Chrome(ChromeDriverManager().install())
   driver = webdriver.Chrome()
elif browserName == "firefox":
    #driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox()
else:
    print("please pass the current broswer name:" + browserName)
    raise Exception("driver is not found")
# driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
time.sleep(5)
driver.find_element(By.ID,'username').send_keys("Saumyasinha@gmail.com")
driver.find_element(By.ID,'password').send_keys("12234@Aqa")
driver.find_element(By.ID,'loginBtn').click()
time.sleep(4)
print(driver.title)
time.sleep(3)