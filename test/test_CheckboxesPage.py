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
        self.checkboxes_page = self.landing_page.go_to_checkboxes()

    def test_checkboxes_page_heading(self):
        """
        Verify the Checkboxes page heading.
        """
        expected_heading = "Checkboxes"
        actual_heading = self.checkboxes_page.get_page_heading().strip()
        logger.info(f"Page heading: {actual_heading}")
        assert expected_heading.lower() == actual_heading.lower(), \
            f"Expected heading '{expected_heading}', but got '{actual_heading}'"

    def test_initial_checkbox_states(self):
        """
        Verify the initial checkbox states:
        - Checkbox 1: unchecked
        - Checkbox 2: checked
        """
        checkbox1_state = self.checkboxes_page.get_checkbox_state(1)
        checkbox2_state = self.checkboxes_page.get_checkbox_state(2)

        logger.info(f"Initial state — Checkbox 1: {checkbox1_state}, Checkbox 2: {checkbox2_state}")
        assert checkbox1_state is False, "Checkbox 1 should be initially unchecked"
        assert checkbox2_state is True, "Checkbox 2 should be initially checked"

    def test_toggle_checkbox_states(self):
        """
        Toggle the checkboxes:
        - Checkbox 1: unchecked → checked
        - Checkbox 2: checked → unchecked
        And validate the toggled states.
        """
        # Toggle checkbox 1 to checked
        if not self.checkboxes_page.get_checkbox_state(1):
            self.checkboxes_page.toggle_checkbox(1)
            logger.info("Checkbox 1 toggled to checked.")

        # Toggle checkbox 2 to unchecked
        if self.checkboxes_page.get_checkbox_state(2):
            self.checkboxes_page.toggle_checkbox(2)
            logger.info("Checkbox 2 toggled to unchecked.")

        # Final state validation
        checkbox1_final = self.checkboxes_page.get_checkbox_state(1)
        checkbox2_final = self.checkboxes_page.get_checkbox_state(2)

        logger.info(f"Final state — Checkbox 1: {checkbox1_final}, Checkbox 2: {checkbox2_final}")
        assert checkbox1_final is True, "Checkbox 1 should be checked after toggling"
        assert checkbox2_final is False, "Checkbox 2 should be unchecked after toggling"

    def test_toggle_both_checkboxes_to_true(self):
        """
        Toggle the checkboxes:
        - Checkbox 1: unchecked → checked
        - Checkbox 2: checked → checked
        And validate the toggled states.
        """
        # Toggle checkbox 1 to checked
        if not self.checkboxes_page.get_checkbox_state(1):
            self.checkboxes_page.toggle_checkbox(1)
            logger.info("Checkbox 1 toggled to checked.")

        # Toggle checkbox 2 to checked
        if not self.checkboxes_page.get_checkbox_state(2):
            self.checkboxes_page.toggle_checkbox(2)
            logger.info("Checkbox 2 toggled to checked.")

        # Final state validation
        checkbox1_final = self.checkboxes_page.get_checkbox_state(1)
        checkbox2_final = self.checkboxes_page.get_checkbox_state(2)

        logger.info(f"Final state — Checkbox 1: {checkbox1_final}, Checkbox 2: {checkbox2_final}")
        assert checkbox1_final is True, "Checkbox 1 should be checked"
        assert checkbox2_final is True, "Checkbox 2 should be checked"

    def test_toggle_both_checkboxes_to_false(self):
        """
        Toggle the checkboxes:
        - Checkbox 1: unchecked → unchecked
        - Checkbox 2: checked → unchecked
        And validate the toggled states.
        """
        # Toggle checkbox 1 to checked
        if self.checkboxes_page.get_checkbox_state(1):
            self.checkboxes_page.toggle_checkbox(1)
            logger.info("Checkbox 1 toggled to unchecked.")

        # Toggle checkbox 2 to checked
        if self.checkboxes_page.get_checkbox_state(2):
            self.checkboxes_page.toggle_checkbox(2)
            logger.info("Checkbox 2 toggled to unchecked.")

        # Final state validation
        checkbox1_final = self.checkboxes_page.get_checkbox_state(1)
        checkbox2_final = self.checkboxes_page.get_checkbox_state(2)

        logger.info(f"Final state — Checkbox 1: {checkbox1_final}, Checkbox 2: {checkbox2_final}")
        assert checkbox1_final is False, "Checkbox 1 should be unchecked"
        assert checkbox2_final is False, "Checkbox 2 should be unchecked"