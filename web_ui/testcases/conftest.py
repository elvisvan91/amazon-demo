"""
@Author Van.Vo
"""
import os
import pytest

from py.xml import html
from datetime import datetime
from web_ui.libs.custom_log import reset_step
from web_ui.libs.webdriver_factory import WebDriverFactory
from web_ui.workflow.ui_constants import BASE_URL


@pytest.yield_fixture()
def setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance(BASE_URL)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    reset_step()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    _browser = request.config.getoption("--browser")
    os.environ['browser'] = _browser
    return _browser


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
