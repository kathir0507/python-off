import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Firefox", help="Type in browser type")
    parser.addoption("--url", action="store", default="https://crux.hmsdev.lan/sitesnap/login", help="url")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'Firefox':
        browser = webdriver.Firefox()
        browser.get("https://crux.hmsdev.lan/sitesnap/login")
        browser.implicitly_wait(10)
        browser.set_window_size(1536,864)
        yield browser
        browser.quit()
    else:
        print 'only chrome is supported at the moment'
        


@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")