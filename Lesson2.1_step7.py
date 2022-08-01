
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
   
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
 
element = browser.find_element (By.ID, 'answer')
element.send_keys(y)
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
option1.click()
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
option1.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(1)

    # закрываем браузер после всех манипуляций
#browser.quit()

   


    
