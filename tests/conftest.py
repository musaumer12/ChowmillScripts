from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

driver = None
def pytest_addoption(parser):

    parser.addoption("--browser_name", action="store", default="chrome")
    # parser.addoption("--Url", action = "store", default = "stage")




@pytest.fixture(scope= "class")
def setup(request):
    global driver
    BrowserName = request.config.getoption("--browser_name")
    #UrlName = request.config.getoption("--Url")
    if BrowserName == "chrome":

        driver = webdriver.Chrome()

    elif BrowserName == "firefox":
        driver = webdriver.Firefox()
    elif BrowserName == "IE":
        driver = webdriver.Edge()
    driver.implicitly_wait(4)
    driver.get("https://app-stage.chowmill.com/signin")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


