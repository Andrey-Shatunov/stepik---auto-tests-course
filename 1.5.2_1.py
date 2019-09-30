from selenium import webdriver
import time


def main():
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/registration2.html")

	required = ['first_class','second_class', 'third_class']

	for req in required:
	    element = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.{0} > input'.format(req))
	    element.send_keys("test")

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


if __name__ == '__main__':
	main()
