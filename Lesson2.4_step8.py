import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100'))
browser.find_element(By.ID, 'book').click()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text                  
y = calc(x)

browser.execute_script("window.scrollBy(0, 400);")

fg = browser.find_element(By.XPATH, '//*[@id="answer"]')
fg.send_keys(y)

browser.find_element(By.XPATH, '//*[@id="solve"]').click()

