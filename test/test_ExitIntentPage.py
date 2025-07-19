import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

#since following test cant be done in headless mode and requires pyautogui to move mouse, we skip it
@pytest.mark.skip
@pytest.mark.usefixtures("browser_instance")
class TestExitIntentPage:
    """
    Test suite for Exit Intent page functionalities.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.exit_intent_page = self.landing_page.go_to_exit_intent()

    def test_exit_intent_page_heading(self):
        """
        Verify the heading of the Exit Intent page.
        """
        expected_heading = "Exit Intent"
        actual_heading = self.exit_intent_page.get_page_heading()
        logger.info(f"Exit Intent page heading found: {actual_heading}")
        assert expected_heading.casefold() in actual_heading.casefold(), f"Expected heading to contain '{expected_heading}'"

    def test_exit_intent_popup_visible(self):
        """
        Verify the exit intent popup is visible when mouse moves to exit area.
        """
        self.exit_intent_page.move_mouse_to_exit_intent()
        assert self.exit_intent_page.is_exit_intent_popup_visible(), "Exit intent popup should be visible after mouse move"

    def test_exit_intent_popup_text(self):
        """
        Verify the text of the exit intent popup.
        """
        expected_text = "This is a modal window"
        # Move mouse to trigger the exit intent popup
        self.exit_intent_page.move_mouse_to_exit_intent()
        # Get the actual text from the popup
        actual_text = self.exit_intent_page.get_exit_intent_popup_text()
        logger.info(f"Exit intent popup text found: {actual_text}")
        # Assert that the expected text is in the actual text
        assert expected_text.casefold() in actual_text.casefold(), f"Expected popup text to contain '{expected_text}'"

    def test_close_exit_intent_popup(self):
        """
        Verify closing the exit intent popup.
        """
        # Move mouse to trigger the exit intent popup
        self.exit_intent_page.move_mouse_to_exit_intent()
        # Close the popup
        self.exit_intent_page.click_close_button()
        # Assert that the popup is no longer visible
        assert not self.exit_intent_page.is_exit_intent_popup_visible(), "Exit intent popup should be closed after clicking close button"

    def test_click_outside_exit_intent_popup(self):
        """
        Verify clicking outside the exit intent popup closes it.
        """
        # Move mouse to trigger the exit intent popup
        self.exit_intent_page.move_mouse_to_exit_intent()
        # Click outside the popup to close it
        self.exit_intent_page.click_outside_modal()
        # Assert that the popup is no longer visible
        assert not self.exit_intent_page.is_exit_intent_popup_visible(), "Exit intent popup should be closed after clicking outside"


