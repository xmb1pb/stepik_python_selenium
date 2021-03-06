import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_text = 'Congratulations! You have successfully registered!'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")


@pytest.fixture
def browser():
    print("\nStarting Chrome browser.................")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    print("\nTest finished........Quit browser........")
    browser.quit()


@pytest.mark.xfail(strict=True)
def test_one(browser):
    url = 'http://suninjuly.github.io/registration1.html'

    browser.get(url)
    input_first = browser.find_element(By.XPATH, '//input[@class="form-control first"]')
    input_first.send_keys('Phil')
    input_last = browser.find_element(By.XPATH, '//input[@class="form-control second"]')
    input_last.send_keys('Romanov')
    input_email = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
    input_email.send_keys('ma@il.ru')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1').text
    assert welcome_text_elt == expected_text, f'Expected {expected_text}, got {welcome_text_elt}'


@pytest.mark.smoke
def test_two(browser):
    url = 'http://suninjuly.github.io/registration2.html'
    browser.get(url)
    input_first = browser.find_element(By.XPATH, '//input[@class="form-control first"]')
    input_first.send_keys('Phil')
    input_last = browser.find_element(By.CLASS_NAME, "form-control second")
    input_last.send_keys('Romanov')
    input_email = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
    input_email.send_keys('ma@il.ru')
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1').text
    assert welcome_text_elt == expected_text, f'Expected {expected_text}, got {welcome_text_elt}'


if __name__ == '__main__':
    pytest.main()
