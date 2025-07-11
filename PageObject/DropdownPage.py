from PageObject.BasePage import BasePage


class DropdownPage(BasePage):
    """
    Page object for the Dropdown page.
    """
    dropdown_locator = "//select[@id='dropdown']"
    heading = "//h3[contains(text(),'Dropdown List')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver

    def get_page_heading(self):
        """
        Get the heading of the Dropdown page.
        :return: The text of the page heading.
        """
        return self.get_text(self.heading)

    def select_option(self, option_text):
        """
        Select an option from the dropdown by visible text.
        :param option_text: The text of the option to select.
        """
        self.dropdown_select(self.dropdown_locator,option_text)

    def get_selected_option_value(self):
        """
        Get the currently selected option from the dropdown.
        :return: The text of the selected option.
        """
        return self.get_attribute(self.dropdown_locator,'value')

    def get_text_from_selected_option(self):
        """
        Get the text of the currently selected option in the dropdown.
        :return: The text of the selected option.
        """
        return self.get_selected_option_text(self.dropdown_locator)