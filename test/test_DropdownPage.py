import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.order(12)
@pytest.mark.usefixtures("browser_instance")
class TestDropdownPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dropdown_page = self.landing_page.go_to_dropdown()

    def test_dropdown_page_heading(self):
        """
        Verify the Dropdown page heading.
        """
        expected_heading = "Dropdown List"
        actual_heading = self.dropdown_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_default_dropdown_selection(self):
        default_value = self.dropdown_page.get_selected_option_value()
        assert default_value == "", "Expected default dropdown value to be empty"

    @pytest.mark.parametrize("option_text,expected_value", [
        ("Option 1", "1"),
        ("Option 2", "2"),
    ])
    def test_select_option(self,option_text, expected_value):
        """
        Verify selecting 'Option 1' from the dropdown works correctly.
        """
        self.dropdown_page.select_option(option_text)
        selected_value = self.dropdown_page.get_selected_option_value()
        selected_text = self.dropdown_page.get_text_from_selected_option()

        logger.info(f"Selected dropdown value: {selected_value}")
        logger.info(f"Selected dropdown text: {selected_text}")

        assert selected_value == expected_value, f"Expected value '{expected_value}', got '{selected_value}'"
        assert selected_text == option_text, f"Expected text '{option_text}', got '{selected_text}'"