import warnings
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Hiển thị cửa sổ Chrome")


@pytest.fixture
def base_url():
    return "https://www.saucedemo.com"


@pytest.fixture
def driver(request):
    options = Options()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(30)
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = item.funcargs.get("driver")
    if browser is None or not (report.when == "call" or report.failed):
        return
    try:
        folder = Path("reports/screenshots")
        folder.mkdir(parents=True, exist_ok=True)
        filename = folder / f"{item.name}-{report.when}.png"
        browser.save_screenshot(str(filename))
        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.png(browser.get_screenshot_as_base64(), name="Minh chứng"))
        report.extras = extras
    except Exception as error:
        warnings.warn(f"Không lưu được minh chứng: {error}", stacklevel=1)
