import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path=r'c:\WEBDRV\chromedriver.exe', options=chrome_options)
browser.implicitly_wait(15)
url='http://suninjuly.github.io/find_link_text'
link_text=str(math.ceil(math.pow(math.pi, math.e)*10000))

browser.get(url)

try:
    link=browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    input4.submit()
    button = browser.find_element_by_css_selector('.button.btn"')
   # button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
#нихрена не работает как положено, но ответ в консоли выдает

