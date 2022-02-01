import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path='C:/WEBDRV/chromedriver.exe', options=chrome_options)
browser.implicitly_wait(15)
url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(url)
    price_house = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.XPATH, '//button[@id="book"]')
    button.click()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)
    answer = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(y)
    button_submit = browser.find_element(By.XPATH, '//button[@id="solve"]')
    button_submit.click()
    alert = browser.switch_to.alert
    result = alert.text.split(': ')[-1]
    print(f'Successful test run. Result is: {result}')
    alert.accept()
except Exception as e:
    print(e)
finally:
    browser.quit()
