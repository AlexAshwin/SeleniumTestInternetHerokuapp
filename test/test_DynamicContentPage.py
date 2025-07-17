import pytest
import logging
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestDynamicContentPage:
    """
    Test suite for the Dynamic Content page.
    """
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dynamic_content_page = self.landing_page.go_to_dynamic_content()

    def test_dynamic_content_page_heading(self):
        """
        Verify the Dynamic Content page heading.
        """
        expected_heading = "Dynamic Content"
        actual_heading = self.dynamic_content_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_validate_content_is_dynamic(self):
        """
        Validate that the content on the Dynamic Content page is dynamic.
        This test checks that the content changes on each visit.
        """
        first_content = self.dynamic_content_page.get_dynamic_content()
        logger.info(f"Initial dynamic content: {first_content}")

        # Refresh the page to get new content
        self.dynamic_content_page.refresh_page()

        second_content = self.dynamic_content_page.get_dynamic_content()
        logger.info(f"Dynamic content after refresh: {second_content}")
        logger.info("Comparing initial and refreshed dynamic content.")
        # Check that the content has changed
        assert first_content != second_content, "Dynamic content did not change after refresh"