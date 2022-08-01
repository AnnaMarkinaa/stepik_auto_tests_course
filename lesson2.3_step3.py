import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text                  
y = calc(x)

fg = browser.find_element(By.XPATH, '//*[@id="answer"]')
fg.send_keys(y)

browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

