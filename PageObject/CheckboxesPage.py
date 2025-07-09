from PageObject.BasePage import BasePage


class CheckboxesPage(BasePage):
    # XPath locators for elements on the Checkboxes Page
    heading = "//h3"
    checkboxes_xpath = "//input[@type='checkbox']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the main heading of the Checkboxes page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

    def get_checkbox_state(self, index: int) -> bool:
        """
        Get the state of a checkbox by its index.
        :param index: The index of the checkbox (1-based).
        :return: True if the checkbox is selected, False otherwise.
        """
        xpath = f"({self.checkboxes_xpath})[{index}]"
        element = self.wait_for_element_visible(xpath)
        return element.is_selected()

    def toggle_checkbox(self, index: int):
        """
        Toggle the state of a checkbox by its index.
        :param index: The index of the checkbox (1-based).
        """
        xpath = f"({self.checkboxes_xpath})[{index}]"
        element = self.wait_for_element_clickable(xpath)
        element.click()