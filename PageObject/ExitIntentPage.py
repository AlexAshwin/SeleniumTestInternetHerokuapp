import pyautogui
from PageObject.BasePage import BasePage

class ExitIntentPage(BasePage):
    """
    ExitIntentPage encapsulates operations for the Exit Intent page.
    """

    # XPath locators for elements on the Exit Intent page.
    heading = "//h3"
    exit_intent_popup = "//div[@class='modal']"
    close_button = "//div[@class='modal-footer']//p"
    exit_intent_popup_title = "//div[@class='modal-title']//h3"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the title of the Exit Intent page.

        :return: Title of the Exit Intent page.
        """
        return self.get_text(self.heading)

    def move_mouse_to_exit_intent(self):
        """
        Move the mouse to the exit intent area to trigger the popup.

        This method simulates moving the mouse to the top of the page,
        which is typically where exit intent popups are triggered.
        """
        # Get screen dimensions
        screen_width, screen_height = pyautogui.size()
        # Optional: disable failsafe if you're running automated tests only
        pyautogui.FAILSAFE = False
        # Step 1: Move to center of screen
        pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=0.5)
        self.wait_for_element_visible(self.heading)
        # Step 2: Move to top of screen to trigger exit intent
        pyautogui.moveTo(screen_width // 2, 5, duration=0.5)

    def is_exit_intent_popup_visible(self):
        """
        Check if the exit intent popup is visible on the page.

        :return: True if the popup is visible, False otherwise.
        """
        try:
            if self.wait_for_element_visible(self.exit_intent_popup):
                return True
        except Exception as e:
            return False

    def get_exit_intent_popup_text(self):
        """
        Get the text of the exit intent popup.

        :return: The text of the exit intent popup.
        """
        self.is_exit_intent_popup_visible()
        return self.get_text(self.exit_intent_popup_title)

    def click_close_button(self):
        """
        Close the entry ad by clicking the close button.
        """
        if self.is_exit_intent_popup_visible():
            self.click(self.close_button)
            self.wait_for_element_to_disappear(self.exit_intent_popup)

    def click_outside_modal(self):
        """
        Click outside the modal to close it.
        """
        if self.is_exit_intent_popup_visible():
            # Click at the center of the screen to close the popup
            self.click("//body")
            self.wait_for_element_to_disappear(self.exit_intent_popup)