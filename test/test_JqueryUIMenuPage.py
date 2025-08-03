import logging
import time

import pytest

from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("browser_instance")
class TestJqueryUIMenuPage:
    """
    Test class for the jQuery UI Menu page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.menu_page = self.landing_page.go_to_jquery_ui_menu()

    def test_menu_page_heading(self):
        """
        Verify the jQuery UI Menu page heading.
        """
        expected_heading = "JQueryUI - Menu"
        actual_heading = self.menu_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_menu_button_status(self):
        """
        Verify that the status of button is enabled/disabled.
        """
        assert self.menu_page.is_menu_option_enabled("Enabled"), "Expected 'Enabled' button to be enabled"
        assert not self.menu_page.is_menu_option_enabled("Disabled"), "Expected 'Disabled' button to be disabled"

    def test_click_back_to_jquery_ui_option(self):
        """
        Verify that clicking the 'Back to jQuery UI' option navigates to the correct page.
        """
        self.menu_page.click_menu_option("Enabled")
        self.menu_page.click_menu_option("Back to Jquery UI")
        assert self.menu_page.get_page_heading() == "JQuery UI", "Expected to return to the jQuery UI Menu page"

    @pytest.mark.run_local
    @pytest.mark.parametrize("option", ["pdf", "csv", "xls"])
    def test_downloads_submenu_triggers_file_download(self, option,request):
        """
        Verify that clicking the 'Downloads' option and its submenu (PDF, CSV, Excel) works correctly.
        :param option: Submenu option under 'Downloads'
        """
        filename= f"menu.{option}"
        self.menu_page.click_menu_option("Enabled")
        self.menu_page.click_menu_option("Downloads")
        self.menu_page.click_menu_option(option)
        time.sleep(10) #wait for the download to complete
        downloaded_file = self.menu_page.get_download_path(request, filename)
        assert downloaded_file is not None and downloaded_file.endswith(filename), \
            f"Expected '{filename}' to be downloaded"

