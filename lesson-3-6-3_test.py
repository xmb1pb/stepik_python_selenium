import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

message = ''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1', ]


def answer():
    return math.log(int(time.time()))


@pytest.fixture
def browser():
    print("\nStarting Chrome browser.................")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    print("\nTest finished........Quit browser........")
    browser.quit()


def collector(text):
    with open('temp.txt', 'a') as file:
        print(text, file=file)



@pytest.mark.parametrize('link', links)
def test_secret_message(browser, link):
    browser.get(link)

    input_textarea = browser.find_element(By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]')
    input_textarea.send_keys(answer())

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]')))
    button.click()
    result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//pre[@class="smart-hints__hint"]'))).text
    if result != 'Correct!':
        collector(result)
    assert result == 'Correct!', f'expected \'Correct!\', got \'{result}\''




if __name__ == '__main__':
    pytest.main()
