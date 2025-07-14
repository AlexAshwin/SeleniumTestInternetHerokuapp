
from PageObject.BasePage import BasePage


class DynamicControlPage(BasePage):
    """
    Dynamic Control Page Object.
    This page allows interaction with dynamic controls such as enabling/disabling checkboxes and input fields.
    """
    # XPaths for elements on the Dynamic Control page
    heading = "//h4"
    checkbox = "//input[@type='checkbox']"
    remove_button = "//button[contains(text(), 'Remove')]"
    enable_button = "//button[contains(text(), 'Enable')]"
    disable_button = "//button[contains(text(), 'Disable')]"
    input_field = "//input[@type='text']"
    loader = "//div[@id='loading']"
    checkbox_message = "//form[@id='checkbox-example']//p[@id='message']"
    input_message = "//form[@id='input-example']//p[@id='message']"
    add_button = "//button[contains(text(), 'Add')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the heading of the Dynamic Control page.
        :return: The text of the page heading.
        """
        return self.get_text(self.heading)

    def get_input_field_value(self):
        """
        Get the value of the input field on the Dynamic Control page.
        :return: The text currently in the input field.
        """
        return self.get_attribute(self.input_field, "value")


    def send_text_to_input_field(self, text: str):
        """
        Send text to the input field on the Dynamic Control page.

        :param text: The text to enter into the input field.
        """
        self.enter_text(self.input_field, text)

    def select_checkbox(self):
        """
        Select the checkbox on the Dynamic Control page.
        """
        self.click(self.checkbox)

    def deselect_checkbox(self):
        """
        Deselect the checkbox on the Dynamic Control page.
        """
        if self.is_element_selected(self.checkbox):
            self.click(self.checkbox)

    def click_remove_button(self):
        """
        Click the 'Remove' button to remove the checkbox from the page.
        """
        self.click(self.remove_button)
        self.wait_for_element_to_disappear(self.loader)
        return self.get_text(self.checkbox_message)

    def add_checkbox(self):
        """
        Click the 'Add' button to add the checkbox back to the page.
        """
        self.click(self.add_button)
        self.wait_for_element_to_disappear(self.loader)
        return self.get_text(self.checkbox_message)

    def is_checkbox_present(self):
        return self.is_element_present(self.checkbox)

    def is_input_field_enabled(self):
        return self.is_element_enabled(self.input_field)

    def click_enable_button(self):
        """
        Click the 'Enable' button to enable the input field.
        """
        self.click(self.enable_button)
        self.wait_for_element_to_disappear(self.loader)
        return self.get_text(self.input_message)

    def click_disable_button(self):
        """
        Click the 'Disable' button to disable the input field.
        """
        self.click(self.disable_button)
        self.wait_for_element_to_disappear(self.loader)
        return self.get_text(self.input_message)

