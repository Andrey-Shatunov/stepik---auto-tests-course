from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	wait = WebDriverWait(browser, 12)
	element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

	browser.find_element_by_id("book").click()



	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text


	element = browser.find_element_by_css_selector('#answer')
	element.send_keys(calc(x))

	button = browser.find_element_by_css_selector("#solve")
	button.click()


if __name__ == '__main__':
	main()