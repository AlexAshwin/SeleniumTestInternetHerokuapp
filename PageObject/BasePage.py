from argparse import Action

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    BasePage encapsulates common Selenium WebDriver operations for all page objects,
    using XPath as the sole locator strategy.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Initialize the BasePage.

        :param driver: Selenium WebDriver instance.
        :param timeout: Default timeout for waits (in seconds).
        """
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str):
        """
        Navigate to the specified URL.

        :param url: The URL to open.
        """
        self.driver.get(url)

    def get_url(self) -> str:
        """
        Get the current URL of the page.

        :return: The current URL as a string.
        """
        return self.driver.current_url

    def refresh_page(self):
        """
        Refresh the current page.
        """
        self.driver.refresh()

    def find_element(self, xpath: str):
        """
        Find a single element on the page using XPath.

        :param xpath: The XPath locator.
        :return: WebElement if found.
        """
        return self.driver.find_element(By.XPATH, xpath)

    def find_elements(self, xpath: str):
        """
        Find multiple elements on the page using XPath.

        :param xpath: The XPath locator.
        :return: List of WebElements.
        """
        return self.driver.find_elements(By.XPATH, xpath)

    def wait_for_element_visible(self, xpath: str, timeout: int = None):
        """
        Wait until the element is visible on the page using XPath.

        :param xpath: The XPath locator.
        :param timeout: Optional timeout override.
        :return: WebElement if visible.
        """
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def wait_for_element_clickable(self, xpath: str, timeout: int = None):
        """
        Wait until the element is clickable using XPath.

        :param xpath: The XPath locator.
        :param timeout: Optional timeout override.
        :return: WebElement if clickable.
        """
        wait_time = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def click(self, xpath: str):
        """
        Click on an element using XPath.

        :param xpath: The XPath locator.
        """
        element = self.wait_for_element_clickable(xpath)
        element.click()

    def enter_text(self, xpath: str, text: str):
        """
        Enter text into an input field using XPath.

        :param xpath: The XPath locator.
        :param text: The text to enter.
        """
        element = self.wait_for_element_visible(xpath)
        element.clear()
        element.send_keys(text)

    def get_title(self) -> str:
        """
        Get the current page title.

        :return: The page title as a string.
        """
        return self.driver.title

    def get_text(self, xpath: str):
        """
        Enter text into an input field using XPath.

        :param xpath: The XPath locator.
        :param text: The text to enter.
        """
        return self.find_element(xpath).text

    def delete_cookies(self):
        """
        Delete all cookies in the current session.
        """
        self.driver.delete_all_cookies()

    def alert_accept(self):
        """
        Accept the current alert.
        """
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        """
        Dismiss the current alert.
        """
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def alert_send_keys(self, text: str):
        """
        Send keys to the current alert.

        :param text: The text to send to the alert.
        """
        alert = self.driver.switch_to.alert
        alert.send_keys(text)

    def get_alert_text(self):
        """
        Get the text of the current alert.

        :return: The text of the alert.
        """
        alert = self.driver.switch_to.alert
        return alert.text

    def execute_script(self, script: str, *args):
        """
        Execute a JavaScript script in the context of the current page.

        :param script: The JavaScript code to execute.
        :param args: Optional arguments to pass to the script.
        :return: The result of the script execution.
        """
        return self.driver.execute_script(script, *args)

    def context_click(self, xpath: str):
        """
        Perform a context click (right-click) on an element using XPath.

        :param xpath: The XPath locator.
        """
        element = self.wait_for_element_visible(xpath)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

