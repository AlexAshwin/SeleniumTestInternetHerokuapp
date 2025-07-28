import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestHoversPage:
    """
    Test class for the Hovers page.
    """
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.hover_page = self.landing_page.go_to_hovers()

    def test_hovers_page_heading(self):
        """
        Verify the Hovers page heading.
        """
        expected_heading = "Hovers"
        actual_heading = self.hover_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_hover_over_users(self):
        """
        Verify hovering over user images reveals correct information.
        """
        user_count = self.hover_page.list_of_users()
        logger.info(f"Number of users found: {user_count}")

        for i in range(1, user_count + 1):
            hover_text = self.hover_page.hover_over_user(i)
            logger.info(f"Hover text for user {i}: {hover_text}")
            assert f"user{i}" in hover_text.lower(), f"Expected hover text to contain 'user{i}'"