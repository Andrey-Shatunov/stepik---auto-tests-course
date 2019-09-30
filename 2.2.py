from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x, y):
  return int(x) + int(y)


def main():
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html")

	x_element = browser.find_element_by_css_selector('#num1')
	x = x_element.text
	y_element = browser.find_element_by_css_selector('#num2')
	y = y_element.text

	z = calc(x, y)

	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(z))

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("body > div > form > button")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)


if __name__ == '__main__':
	main()