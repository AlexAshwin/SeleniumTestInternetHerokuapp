import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.order(2)
@pytest.mark.usefixtures("browser_instance")
class TestABTestingPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.ab_testing_page = self.landing_page.go_to_ab_testing()

    @pytest.mark.xfail
    @pytest.mark.repeat(3)
    def test_ab_testing_page_heading(self):
        """
        Verify the AB Testing page heading.
        """
        expected_heading = "A/B Test Control"
        actual_heading = self.ab_testing_page.get_ab_testing_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"
