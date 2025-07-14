from argparse import Action

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


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

    def wait_for_element_to_disappear(self,xpath:str, timeout: int = None ):
        """
        Wait for the loader element to disappear (become invisible or removed from DOM).
        """
        wait_time = timeout if timeout is not None else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.invisibility_of_element_located((By.XPATH,xpath))
            )
        except TimeoutException:
            raise TimeoutException("Loader did not disappear within the timeout.")

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

    def drag_and_drop(self, source_xpath: str, target_xpath: str):
        """
        Perform a drag and drop operation from one element to another using XPath.

        :param source_xpath: The XPath locator of the source element.
        :param target_xpath: The XPath locator of the target element.
        """
        source = self.wait_for_element_visible(source_xpath)
        target = self.wait_for_element_visible(target_xpath)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def dropdown_select(self, dropdown_xpath: str, option_text: str):
        """
        Select an option from a dropdown by visible text.

        :param dropdown_xpath: The XPath locator of the dropdown element.
        :param option_text: The text of the option to select.
        """
        dropdown_element = self.wait_for_element_visible(dropdown_xpath)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    def get_attribute(self,xpath: str, attribute_name: str):
        """
        Get the value of an attribute from an element using XPath.

        :param xpath: The XPath locator.
        :param attribute_name: The name of the attribute to retrieve.
        :return: The value of the specified attribute.
        """
        element = self.find_element(xpath)
        return element.get_attribute(attribute_name)

    def get_selected_option_text(self, dropdown_xpath: str):
        """
        Get the text of the currently selected option in a dropdown.

        :param dropdown_xpath: The XPath locator of the dropdown element.
        :return: The text of the selected option.
        """
        dropdown_element = self.wait_for_element_visible(dropdown_xpath)
        select = Select(dropdown_element)
        return select.first_selected_option.text

    def is_element_selected(self, xpath: str) -> bool:
        """
        Check if an element is selected (e.g., checkbox or radio button).

        :param xpath: The XPath locator of the element.
        :return: True if the element is selected, False otherwise.
        """
        element = self.find_element(xpath)
        return element.is_selected() if element else False

    def is_element_visible(self, xpath: str) -> bool:
        """
        Check if an element is visible on the page.

        :param xpath: The XPath locator of the element.
        :return: True if the element is visible, False otherwise.
        """
        try:
            element = self.find_element(xpath)
            return element.is_displayed()
        except Exception:
            return False

    def is_element_present(self, xpath: str) -> bool:
        """
        Check if an element is present in the DOM.

        :param xpath: The XPath locator of the element.
        :return: True if the element is present, False otherwise.
        """
        try:
            self.find_element(xpath)
            return True
        except Exception:
            return False

    def is_element_enabled(self,xpath: str) -> bool:
        """
        Check if an element is enabled (e.g., input field, button).

        :param xpath: The XPath locator of the element.
        :return: True if the element is enabled, False otherwise.
        """
        try:
            element = self.find_element(xpath)
            return element.is_enabled()
        except Exception:
            return False