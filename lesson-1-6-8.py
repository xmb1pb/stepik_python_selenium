from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path=r'c:\WEBDRV\chromedriver.exe', options=chrome_options)
url='http://suninjuly.github.io/registration1.html'
browser.implicitly_wait(10)

try:
    browser.get(url)
    input_first=browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input_first.send_keys('Phil')
    input_last = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input_last.send_keys('Romanov')
    input_email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input_email.send_keys('ma@il.ru')

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
    assert "Congratulations! You have successfully registered!" == welcome_text
except Exception as e:
    print(e)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()