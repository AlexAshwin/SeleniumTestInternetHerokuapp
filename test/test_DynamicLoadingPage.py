import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestDynamicLoadingPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dynamic_loading_page = self.landing_page.go_to_dynamic_loading()

    def test_dynamic_loading_page_heading(self):
        """
        Verify the Dynamic Loading page heading.
        """
        expected_heading = "Dynamically Loaded Page Elements"
        actual_heading = self.dynamic_loading_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

class TestDynamicLoadingExample1Page:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dynamic_loading_page = self.landing_page.go_to_dynamic_loading()
        self.dynamic_loading_example1_page = self.dynamic_loading_page.go_to_example1()

    def test_element_default_invisible(self):
        """
        Verify the loading message is not visible by default.
        """
        assert not self.dynamic_loading_example1_page.is_message_visible(), "Loading message should not be visible initially"

    def test_element_visible_after_start(self):
        """
        Verify the loading message becomes visible after clicking the start button.
        """
        self.dynamic_loading_example1_page.click_start_button()
        assert self.dynamic_loading_example1_page.is_message_visible(), "Loading message should be visible after clicking start button"


class TestDynamicLoadingExample2Page:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dynamic_loading_page = self.landing_page.go_to_dynamic_loading()
        self.dynamic_loading_example2_page = self.dynamic_loading_page.go_to_example2()

    def test_element_default_invisible(self):
        """
        Verify the loading message is not visible by default.
        """
        assert not self.dynamic_loading_example2_page.is_message_visible(), "Loading message should not be visible initially"

    def test_element_visible_after_start(self):
        """
        Verify the loading message becomes visible after clicking the start button.
        """
        self.dynamic_loading_example2_page.click_start_button()
        assert self.dynamic_loading_example2_page.is_message_visible(), "Loading message should be visible after clicking start button"