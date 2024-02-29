from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
#multiple selection of drop down
def select_values(option_list,value):
    if not value[0]=='all':
        for ele in dropdown_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    time.sleep(2)
                    break
    else:
        try:

            for ele in option_list:
                ele.click()
        except Exception as e:
            print(e)



driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(3)
driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(5)
dropdown_list =driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
#multiple selection of dropdwon_all values
#value_list=['all']
value_list=['choice 7']
# for selecting only selected values
#value_list=['choice 2', 'choice 3', 'choice 6 2 1']
select_values(dropdown_list,value_list)
time.sleep(2)
# select_values(dropdown_list,'choice 1')
# select_values(dropdown_list,'choice 6 2 1')