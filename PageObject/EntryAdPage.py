from PageObject.BasePage import BasePage

class EntryAdPage(BasePage):
    """
    EntryAdPage encapsulates operations for the Entry Ad page.
    """

    # XPath locators for elements on the Entry Ad page.
    modal = "//div[@id='modal']"
    modal_title = "//div[@class='modal-title']//h3"
    modal_close_button = "//div[@class='modal-footer']/p"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_pop_up_visible(self):
        """
        Check if the entry ad pop-up is visible on the page.

        :return: True if the pop-up is visible, False otherwise.
        """
        try:
            if self.wait_for_element_visible(self.modal):
                return True
        except Exception as e:
            return False

    def get_pop_up_title(self):
        """
        Get the title of the entry ad pop-up.

        :return: The text of the pop-up title.
        """
        self.is_pop_up_visible()
        return self.get_text(self.modal_title)

    def click_close_button(self):
        """
        Close the entry ad by clicking the close button.
        """
        if self.is_pop_up_visible():
            self.click(self.modal_close_button)
            self.wait_for_element_to_disappear(self.modal)

    def click_outside_modal(self):
        """
        Click outside the modal to close it.
        """
        if self.is_pop_up_visible():
            self.click("//body")
            self.wait_for_element_to_disappear(self.modal)