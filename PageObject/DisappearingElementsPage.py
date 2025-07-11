from PageObject.BasePage import BasePage


class DisappearingElementsPage(BasePage):
    # XPath locators for elements on the Context Menu Page
    heading = "//h3"
    elements = "//ul//a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the main heading of the Disappearing Elements page.
        """
        return self.get_text(self.heading)


    def elements_text(self):
        """
        Get the text of all disappearing elements on the page.
        :return: List of texts of the elements.
        """
        return [element.text for element in self.find_elements(self.elements)]
