from PageObject.BasePage import BasePage


class DigestAuthPage(BasePage):
    """
    Page Object for the Digest Authentication page.
    """
    # XPath locators for elements on the Digest Authentication Page
    heading = "//h3"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_url(self):
        """
        Get the URL of the Digest Authentication page.
        :return: URL of the page.
        """
        return self.get_url()

    def get_page_heading(self):
        """
        Get the main heading of the Digest Authentication page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

