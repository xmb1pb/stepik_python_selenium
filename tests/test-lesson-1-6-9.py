import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test169(unittest.TestCase):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)

    def test_one(self):
        url = 'http://suninjuly.github.io/registration1.html'
        expected_text = 'Congratulations! You have successfully registered!'
        self.browser.get(url)
        input_first = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input_first.send_keys('Phil')
        input_last = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input_last.send_keys('Romanov')
        input_email = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input_email.send_keys('ma@il.ru')
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(welcome_text_elt, expected_text)

    def test_two(self):
        url = 'http://suninjuly.github.io/registration2.html'
        expected_text = 'Congratulations! You have successfully registered!'
        self.browser.get(url)
        input_first = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input_first.send_keys('Phil')
        input_last = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input_last.send_keys('Romanov')
        input_email = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input_email.send_keys('ma@il.ru')
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(welcome_text_elt, expected_text)


if __name__ == '__main__':
    unittest.main()
    Test169.browser.quit()
