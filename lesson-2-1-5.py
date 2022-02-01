import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(executable_path=r'C:\WEBDRV\chromedriver.exe', options=chrome_options)
browser.implicitly_wait(10)
url = 'http://suninjuly.github.io/math.html'

try:
    browser.get(url)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    print(x)
    y = calc(int(x))
    print(y)
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(str(y))
    checkbox = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    radiobutton = browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
except Exception as e:
    print(e)
finally:
    time.sleep(10)
    browser.quit()
