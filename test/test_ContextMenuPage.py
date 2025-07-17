import logging

import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestContextMenuPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.context_menu_page = self.landing_page.go_to_context_menu()

    def test_context_menu_page_heading(self):
        """
        Verify the Context Menu page heading.
        """
        expected_heading = "Context Menu"
        actual_heading = self.context_menu_page.get_page_heading().strip()
        logger.info(f"Page heading: {actual_heading}")
        assert expected_heading.lower() == actual_heading.lower(), \
            f"Expected heading '{expected_heading}', but got '{actual_heading}'"

    def test_right_click_box(self):
        """
        Perform a right-click on the context menu box and verify the action.
        """
        self.context_menu_page.right_click_box()
        # Assuming right-click opens an alert, we can check for it
        alert_text = self.context_menu_page.get_alert_text()
        logger.info(f"Alert text: {alert_text}")
        assert alert_text == 'You selected a context menu', "Alert text mismatch."
        logger.info(f"Performing alert accept action after right-click.")
        self.context_menu_page.alert_accept()  # Accept the alert to close it
        logger.info("Right-click action performed and alert accepted.")