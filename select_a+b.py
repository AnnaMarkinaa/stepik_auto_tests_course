from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

a_el = browser.find_element(By.XPATH, '/html/body/div/form/h2/span[2]')
a = a_el.text
b_el = browser.find_element(By.XPATH, '/html/body/div/form/h2/span[4]')
b = b_el.text
x2 = str(int(a)+int(b))  #сложили два числа

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(x2)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)
