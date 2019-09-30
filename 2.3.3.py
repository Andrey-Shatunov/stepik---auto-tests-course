from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

element = browser.find_element_by_class_name('trollface.btn.btn-primary')
element.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
# confirm = browser.switch_to.alert
# confirm.accept()


x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text


z = calc(x)

element = browser.find_element_by_css_selector('#answer')
element.send_keys(z)

button = browser.find_element_by_tag_name("button")
button.click()


# Отправляем заполненную форму

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)




