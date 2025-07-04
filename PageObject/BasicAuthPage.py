
from PageObject.BasePage import BasePage


class BasicAuthPage(BasePage):
    """
    Page object for the Basic Authentication page.
    Inherits common Selenium operations from BasePage.
    """

    message = "//div[@class='example']//p"
    basicauth = "//a[text()='Basic Auth']"  # Update this XPath as needed for your app

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_basic_auth(self):
        """
        Clicks the Basic Auth link/button to navigate to the Basic Authentication page.
        """
        self.click(self.basicauth)

    def get_page_heading(self):
        """
        Get the main heading of the Basic Authentication page.
        :return: Main heading text.
        """
        return self.get_text(self.message)
