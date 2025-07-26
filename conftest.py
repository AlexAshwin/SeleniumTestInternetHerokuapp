import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator

# Configure logging once at the module level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

# ---------------------------
# PyTest CLI Options
# ---------------------------
def pytest_addoption(parser):
    parser.addoption(
        "--use_grid",
        action="store",
        default="false",
        help="Use Selenium Grid: true or false"
    )

# ---------------------------
# Pre-test Session Setup
# ---------------------------
def pytest_sessionstart(session):
    """
    Called before test session starts — cleans up previous reports.
    """
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")

    if os.path.exists(reports_dir):
        logger.info(f"Removing existing reports directory: {reports_dir}")
        import shutil
        shutil.rmtree(reports_dir)

    os.makedirs(os.path.join(reports_dir, "downloads"), exist_ok=True)
    os.makedirs(os.path.join(reports_dir, "screenshots"), exist_ok=True)
    logger.info("✅ Fresh reports directory created.")

# ---------------------------
# Utility: Download Directory Path
# ---------------------------
def download_dir() -> str:
    """
    Returns the absolute path to the download directory inside reports.
    Assumes it's already created in pytest_sessionstart.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(project_root, "reports", "downloads")

# ---------------------------
# WebDriver Fixture
# ---------------------------
@pytest.fixture(scope="function")
def browser_instance(request) -> Generator[WebDriver, None, None]:
    """
    Provides a Selenium WebDriver instance configured for local or grid execution.
    Cleans up after test.
    """
    use_grid = request.config.getoption("use_grid").strip().lower() == "true"
    grid_url = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

    download_path = download_dir()
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    #options.add_argument("--headless=new")

    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.geolocation": 1
    })

    driver = (
        webdriver.Remote(command_executor=grid_url, options=options)
        if use_grid else
        webdriver.Chrome(options=options)
    )

    driver.implicitly_wait(5)
    request.node._driver = driver
    request.node._download_path = download_path

    yield driver
    driver.quit()

# ---------------------------
# Hook: Screenshot + Download Attachments
# ---------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Attach screenshots and downloaded files to the HTML report on test failure.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")
        driver = getattr(item._request.node, "_driver", None)

        # Attach screenshot on failure
        if (report.failed and not xfail) or (report.skipped and xfail):
            if driver:
                file_name = _screenshot_path(report.nodeid)
                driver.save_screenshot(file_name)
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        # Attach downloaded files
        download_path = getattr(item._request.node, "_download_path", None)
        if download_path and os.path.exists(download_path):
            for file in os.listdir(download_path):
                file_path = os.path.join(download_path, file)
                if os.path.isfile(file_path):
                    rel_path = os.path.relpath(file_path, os.path.dirname(__file__))
                    html_link = f'<div><a href="{rel_path}" target="_blank">📥 {file}</a></div>'
                    extra.append(pytest_html.extras.html(html_link))

    report.extras = extra

# ---------------------------
# Utility: Screenshot Path Builder
# ---------------------------
def _screenshot_path(nodeid: str) -> str:
    """
    Build a sanitized file path for saving screenshots based on the test nodeid.
    """
    sanitized_nodeid = nodeid.replace("::", "_").replace("/", "_").replace("\\", "_").replace(" ", "_")
    reports_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
    return os.path.join(reports_dir, f"{sanitized_nodeid}.png")
