from PageObject.BasePage import BasePage


class ContextMenuPage(BasePage):
    # XPath locators for elements on the Context Menu Page
    heading = "//h3"
    box = "//div[@id='hot-spot']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the main heading of the Context Menu page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

    def right_click_box(self):
        """
        Perform a right-click action on the context menu box.
        :return: None
        """
        self.context_click(self.box)
