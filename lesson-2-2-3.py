import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")


def calc(x,y):
    return str(int(x)+int(y))


browser = webdriver.Chrome(executable_path=r'C:\WEBDRV\chromedriver.exe', options=chrome_options)
browser.implicitly_wait(10)
url = 'http://suninjuly.github.io/selects2.html'

try:
    browser.get(url)
    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    print(x)
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text
    print(y)
    z=calc(x,y)
    selection=Select(browser.find_element(By.ID, 'dropdown'))
    selection.select_by_value(z)
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
except Exception as e:
    print(e)
finally:
    time.sleep(10)
    browser.quit()

