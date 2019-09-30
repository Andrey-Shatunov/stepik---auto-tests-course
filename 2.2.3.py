from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os


def main():
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/file_input.html")

	elements = browser.find_elements_by_class_name('form-control')
	for element in elements:
		element.send_keys('olo')

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')

	element = browser.find_element_by_css_selector('#file')
	element.send_keys(file_path)



	# select = Select(browser.find_element_by_tag_name("select"))
	# select.select_by_value(str(z))
	# element = browser.find_element_by_css_selector('#answer')
	# element.send_keys(y)
	button = browser.find_element_by_tag_name("button")
	button.click()


	# Отправляем заполненную форму

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)


if __name__ == '__main__':
	main()




