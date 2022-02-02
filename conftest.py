import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption('browser_name')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = None
    if browser_name in ('Chrome', 'chrome'):
        print('Launch Chrome browser ..........')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name in ('Firefox','firefox'):
        print('Launch FIrefox browser ..........')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
