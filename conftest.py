import os
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator
import logging

logger = logging.getLogger(__name__)


# ---------------------------
# PyTest Options
# ---------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome,firefox",
        help="Comma-separated list of browsers to test with, e.g. chrome,firefox"
    )
    parser.addoption(
        "--use_grid",
        action="store",
        default="false",
        help="Use Selenium Grid: true or false"
    )
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    )


# ---------------------------
# This function is a pytest hook that dynamically parameterizes tests based on the browser_name command-line option,
# allowing tests to run with different browser configurations
# ---------------------------
def pytest_generate_tests(metafunc):
    # Check if the test function uses the 'browser_name' fixture
    if "browser_name" in metafunc.fixturenames:
        # Retrieve the value of the '--browser_name' command-line option and split by commas
        selected_browsers = metafunc.config.getoption("browser_name").split(",")
        # Parameterize the test so it runs once for each specified browser
        # (after stripping whitespace and converting to lowercase)
        metafunc.parametrize("browser_name", [b.strip().lower() for b in selected_browsers])


# ---------------------------
# Browser Instance Fixture
# returns a WebDriver instance based on the specified browser name.
# ---------------------------
@pytest.fixture(scope="function")
def browser_instance(browser_name, request) -> Generator[WebDriver, None, None]:
    use_grid = request.config.getoption("use_grid").strip().lower() == "true"
    grid_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

    driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })

        driver = webdriver.Remote(command_executor=grid_url, options=options) if use_grid else webdriver.Chrome(
            options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("signon.autofillForms", False)
        options.set_preference("security.insecure_field_warning.contextual.enabled", False)

        driver = webdriver.Remote(command_executor=grid_url, options=options) if use_grid else webdriver.Firefox(
            options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    request.node._driver = driver  # attach to node for screenshot capture
    yield driver
    driver.quit()


# ---------------------------
# Screenshot Capture on Failure
# ---------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")
        if (report.failed and not xfail) or (report.skipped and xfail):
            driver = getattr(item._request.node, "_driver", None)
            if driver:
                file_name = _screenshot_path(report.nodeid)
                os.makedirs(os.path.dirname(file_name), exist_ok=True)
                driver.save_screenshot(file_name)
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

    report.extra = extra


# ---------------------------
# Utilities
# Defines a utility function that takes a test node ID (as a string) and returns a string.
# The type hints indicate both the input and output are strings.
# ---------------------------
def _screenshot_path(nodeid: str) -> str:
    sanitized_nodeid = nodeid.replace("::", "_").replace("/", "_").replace("\\", "_").replace(" ", "_")
    logger.info(f"Sanitized nodeid: {sanitized_nodeid}")
    reports_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
    logger.info(f"Saving screenshot to: {reports_dir}")
    return os.path.join(reports_dir, f"{sanitized_nodeid}.png")
