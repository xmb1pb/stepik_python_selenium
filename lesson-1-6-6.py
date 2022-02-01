from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path=r'c:\WEBDRV\chromedriver.exe', options=chrome_options)
browser.implicitly_wait(15)
url='http://suninjuly.github.io/huge_form.html'

try:
    browser.get(url)
    input_fields=browser.find_elements(By.XPATH, '//input')
    for i in input_fields:
        i.send_keys('qwerty')
    btn=browser.find_element(By.XPATH, '//button').click()
finally:
    time.sleep(10)
    browser.quit()