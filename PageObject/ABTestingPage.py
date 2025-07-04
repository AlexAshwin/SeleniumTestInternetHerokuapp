from PageObject.BasePage import BasePage


class ABTestingPage(BasePage):

    #XPath locators for elements on the AB Testing page
    heading = "//h3"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_ab_testing_page_heading(self):
        """
        Get the title of the AB Testing page.

        :return: Title of the AB Testing page.
        """
        return self.get_text(self.heading)
