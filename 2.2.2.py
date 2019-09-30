from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))


def main():
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/execute_script.html")

		x_element = browser.find_element_by_css_selector('#input_value')
		x = x_element.text

		z = calc(x)

		button = browser.find_element_by_tag_name("button")

		element = browser.find_element_by_css_selector('#answer')
		browser.execute_script("return arguments[0].scrollIntoView(true);", element)
		element.send_keys(z)
		browser.find_element_by_css_selector('#robotsRule').click()
		browser.find_element_by_css_selector('#robotCheckbox').click()

		browser.execute_script("return arguments[0].scrollIntoView(true);", button)
		button.click()

		# Отправляем заполненную форму

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
		
if __name__ == '__main__':
	main()