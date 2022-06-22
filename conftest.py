import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose user language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options,executable_path="E:\\chromedriver\\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()