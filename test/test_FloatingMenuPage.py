import logging

import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestFloatingMenuPage:
    """
    Test class for Floating Menu Page.
    """
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.floating_menu_page = self.landing_page.go_to_floating_menu()

    def test_floating_menu_page_heading(self):
        """
        Verify the heading of the Floating Menu page.
        """
        expected_heading = "Floating Menu"
        actual_heading = self.floating_menu_page.get_page_heading()
        logger.info(f"Floating Menu page heading found: {actual_heading}")
        assert expected_heading.casefold() in actual_heading.casefold(), f"Expected heading to contain '{expected_heading}'"

    def test_floating_menu_visibility(self):
        """
        Verify the visibility of the floating menu at the top, middle and bottom of page.
        """
        # Check visibility at the top of the page
        self.floating_menu_page.scroll_to_top_of_page()
        assert self.floating_menu_page.is_menu_visible(), "Floating menu should be visible at the top of the page"
        assert self.floating_menu_page.get_menu_items() == ["Home", "News","Contact", "About"],\
                                                            "Menu items should match expected values"
        # Check visibility in the middle of the page
        self.floating_menu_page.scroll_to_middle_of_page()
        assert self.floating_menu_page.is_menu_visible(), "Floating menu should be visible in the middle of the page"
        assert self.floating_menu_page.get_menu_items() == ["Home", "News","Contact","About"],\
                                                            "Menu items should match expected values"
        # Check visibility at the bottom of the page
        self.floating_menu_page.scroll_to_end_of_page()
        assert self.floating_menu_page.is_menu_visible(), "Floating menu should be visible at the bottom of the page"
        assert self.floating_menu_page.get_menu_items() == ["Home", "News","Contact","About"],\
                                                            "Menu items should match expected values"