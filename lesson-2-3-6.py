import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x)->str:
    return str(math.log(abs(12 * math.sin(int(x)))))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path='C:/WEBDRV/chromedriver.exe', options=chrome_options)
browser.implicitly_wait(10)
url = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(url)
    old_window=browser.window_handles[0]
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    x=browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y=calc(x)
    answer=browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    submit_button=browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
    alert=browser.switch_to.alert
    result=alert.text.split(': ')[-1]
    print(f'Successful test run. Result is: {result}')
    alert.accept()
except Exception as e:
    print(e)
finally:
    browser.quit()
