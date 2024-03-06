import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
#options = webdriver.Chrome()
#options.headless=True
#driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.reddit.com/')
#first way to do
driver.get_screenshot_as_file(' reddit.png')
#make sure that you are running in headless mode for full screen shot
s=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(s('Width'),s('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('redditfull.png')