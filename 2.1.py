from selenium import webdriver
import time
import math


def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

def main():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)


    element = browser.find_element_by_css_selector('#answer')
    element.send_keys(y)


    #robotCheckbox
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

if __name__ == '__main__':
    main()



