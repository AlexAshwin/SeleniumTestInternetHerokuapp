
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


    def get_page_message(self):
        """
        Get the main heading of the Basic Authentication page.
        :return: Main heading text.
        """
        return self.get_text(self.message)
