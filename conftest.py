import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: it, fr, en etc")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    print("\nstart chrome browser for test..")
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
