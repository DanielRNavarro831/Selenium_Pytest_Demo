import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

browser_used = "Chrome"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=browser_used,
                     help="Specify which browser will be used: chrome, firefox, or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser: str):
    browser = browser.title()
    global driver
    global browser_used
    if browser == "Chrome":
        driver = webdriver.Chrome()
        browser_used = "Chrome"
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        browser_used = "Firefox"
    elif browser == "Edge":
        driver = webdriver.Edge()
        browser_used = "Edge"
    else:
        raise ValueError(f"Unsupported Browser Option: {browser}")
    return driver


def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Pytest Demo, nopcommerce'
    config.stash[metadata_key]['Browser'] = browser_used


@pytest.mark.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

# To generate an HTML report, use: pytest -s -v --html .\reports\report.html
