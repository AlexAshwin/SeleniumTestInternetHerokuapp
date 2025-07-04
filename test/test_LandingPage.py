import pytest
import logging
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.order(1)
@pytest.mark.usefixtures("browser_instance")
class TestLandingPage:

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()

    def test_landing_page_title(self):
        """
        Verify the page title.
        """
        expected_title = "The Internet"
        actual_title = self.landing_page.get_landing_page_title()
        logger.info(f"Title found: {actual_title}")
        assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"


    def test_landing_page_heading(self):
        """
        Verify the main heading.
        """
        expected_heading = "Welcome to the-internet"
        actual_heading = self.landing_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"
