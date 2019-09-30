from selenium import webdriver


def main():
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/find_xpath_form")
	elements = browser.find_elements_by_tag_name('input')
	for element in elements:
	    element.send_keys("Мой ответ")

	button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
	button.click()


if __name__ == '__main__':
	main()