import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.order(14)
@pytest.mark.usefixtures("browser_instance")
class TestDynamicControlPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test to initialize the landing page and navigate to the dynamic control page.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.dynamic_control_page = self.landing_page.go_to_dynamic_control()

    def test_dynamic_control_page_heading(self):
        """
        Verifies that the Dynamic Control page displays the correct heading.
        """
        expected_heading = "Dynamic Controls"
        actual_heading = self.dynamic_control_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_select_checkbox(self):
        """
        Verifies that the checkbox can be selected on the Dynamic Control page.
        """
        self.dynamic_control_page.select_checkbox()
        logger.info("Checkbox selected")
        assert self.dynamic_control_page.is_element_selected(self.dynamic_control_page.checkbox), "Checkbox should be selected"

    def test_select_checkbox_and_click_remove_button(self):
        """
        Verifies that the checkbox can be selected and removed from the page.
        """
        self.dynamic_control_page.select_checkbox()
        logger.info("Checkbox selected, now clicking 'Remove' button")
        message = self.dynamic_control_page.click_remove_button()
        logger.info(f"Remove message displayed: {message}")
        assert "It's gone!" in message, "Expected message 'It's gone!' after removing checkbox"
        assert not self.dynamic_control_page.is_checkbox_present(), "Checkbox should be removed from the page"

    def test_remove_checkbox_without_selecting_and_then_enabling_it(self):
        """
        Verifies that the checkbox can be removed without selecting it, added back, and selected again.
        """
        logger.info("Clicking 'Remove' button without selecting checkbox")
        message = self.dynamic_control_page.click_remove_button()
        logger.info(f"Remove message displayed: {message}")
        assert "It's gone!" in message, "Expected message 'It's gone!' after removing checkbox"
        assert not self.dynamic_control_page.is_checkbox_present(), "Checkbox should be removed from the page"

        logger.info("Now clicking 'Add' button to re-add checkbox")
        message = self.dynamic_control_page.add_checkbox()
        logger.info(f"Add message displayed: {message}")
        assert "It's back!" in message, "Expected message 'It's back!' after adding checkbox"
        assert self.dynamic_control_page.is_checkbox_present(), "Checkbox should be present after re-adding"

        self.dynamic_control_page.select_checkbox()
        logger.info("Checkbox selected after adding it back")
        assert self.dynamic_control_page.is_element_selected(self.dynamic_control_page.checkbox), "Checkbox should be selected after adding it back"

    def test_validate_input_field_disabled(self):
        """
        Verifies that the input field is disabled by default.
        """
        logger.info("Checking if input field is disabled by default")
        assert not self.dynamic_control_page.is_input_field_enabled(), "Input field should be disabled by default"

    def test_cannot_send_keys_to_disabled_input_field(self):
        """
        Verifies that sending keys to a disabled input field raises an exception.
        """
        logger.info("Attempting to send text to disabled input field")
        with pytest.raises(Exception):  # Adjust if you want a specific exception type
            self.dynamic_control_page.send_text_to_input_field("Should fail")

    @pytest.mark.smoke
    def test_enable_input_field_and_send_keys(self):
        """
        Verifies enabling the input field and sending text successfully.
        """
        logger.info("Clicking 'Enable' button")
        input_message = self.dynamic_control_page.click_enable_button()
        logger.info(f"Message after enabling input: {input_message}")

        assert self.dynamic_control_page.is_input_field_enabled(), "Input field should be enabled after clicking 'Enable' button"
        assert "It's enabled!" in input_message, "Expected message 'It's enabled!' after enabling input field"

        self.dynamic_control_page.send_text_to_input_field("Test input")
        input_value = self.dynamic_control_page.get_input_field_value()
        logger.info(f"Input field value after sending text: {input_value}")
        assert input_value == "Test input", "Input field should contain the text 'Test input' after sending keys"

    def test_disable_input_field_preserves_value(self):
        """
        Verifies that disabling the input field retains the entered value.
        """
        logger.info("Enabling input field and entering text")
        self.dynamic_control_page.click_enable_button()
        self.dynamic_control_page.send_text_to_input_field("Final test")

        logger.info("Disabling input field")
        self.dynamic_control_page.click_disable_button()
        assert not self.dynamic_control_page.is_input_field_enabled(), "Input field should be disabled after clicking 'Disable'"

        retained_value = self.dynamic_control_page.get_input_field_value()
        logger.info(f"Input field value after disabling: {retained_value}")
        assert retained_value == "Final test", "Text should remain after input field is disabled"