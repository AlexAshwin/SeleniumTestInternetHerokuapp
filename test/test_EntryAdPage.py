import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestEntryAdPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.entry_ad_page = self.landing_page.go_to_entry_ad()

    def test_entry_ad_pop_up_visible(self):
        """
        Verify the entry ad pop-up is visible.
        """
        assert self.entry_ad_page.is_pop_up_visible(), "Entry ad pop-up should be visible"

    def test_entry_ad_title(self):
        """
        Verify the title of the entry ad pop-up.
        """
        expected_title = "This is a modal window"
        actual_title = self.entry_ad_page.get_pop_up_title()
        logger.info(f"Pop-up title found: {actual_title}")
        assert expected_title.casefold() in actual_title.casefold(), f"Expected title to contain '{expected_title}'"

    def test_close_entry_ad(self):
        """
        Verify closing the entry ad pop-up.
        """
        self.entry_ad_page.click_close_button()
        assert not self.entry_ad_page.is_pop_up_visible(), "Entry ad pop-up should be closed"

    def test_click_outside_modal(self):
        """
        Verify clicking outside the modal closes it.
        """
        self.entry_ad_page.click_outside_modal()
        assert not self.entry_ad_page.is_pop_up_visible(), "Entry ad pop-up should be closed after clicking outside"