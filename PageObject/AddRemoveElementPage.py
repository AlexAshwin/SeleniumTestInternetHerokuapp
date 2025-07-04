from PageObject.BasePage import BasePage


class AddRemoveElementPage(BasePage):
    """
    Page object for the Add/Remove Elements page.
    Inherits common Selenium operations from BasePage.
    """

    # Example XPath locators for elements on the Add/Remove Elements page
    add_element_button = "//button[text()='Add Element']"
    delete_buttons = "//button[text()='Delete']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def add_element(self):
        """
        Click the button to add a new element.
        """
        self.click(self.add_element_button)

    def get_delete_buttons_count(self):
        """
        Get the count of delete buttons present on the page.

        :return: Number of delete buttons.
        """
        return len(self.find_elements(self.delete_buttons))

    def delete_element(self, index=0):
        """
        Click the delete button for a specific element by index.

        :param index: Index of the delete button to click (default is 0).
        """
        delete_buttons = self.find_elements(self.delete_buttons)
        if index < len(delete_buttons):
            delete_buttons[index].click()

    def get_random_count(self):
       """
       get a random number
       :return: int
       """
       import random
       return random.randint(1, 5)