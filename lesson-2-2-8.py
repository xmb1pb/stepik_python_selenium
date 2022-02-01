import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path=r'C:\WEBDRV\chromedriver.exe', options=chrome_options)
browser.implicitly_wait(10)
url = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(url)
    input_name = browser.find_element(By.NAME, 'firstname')
    input_name.send_keys('Salmon')
    input_lastname = browser.find_element(By.NAME, 'lastname')
    input_lastname.send_keys('Tuna')
    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys('head@crab.sea')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_loader=browser.find_element(By.NAME, 'file')
    file_loader.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

except Exception as e:
    print(e)
finally:
    time.sleep(10)
    browser.quit()
