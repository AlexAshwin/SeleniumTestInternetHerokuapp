import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestDisappearingElementsPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.disappearing_element_page = self.landing_page.go_to_disappearing_elements()

    def test_disappearing_elements(self):
        """
        Test to verify the disappearing elements functionality.
        """
        # Get the initial count of elements
        initial_list = self.disappearing_element_page.elements_text()
        logger.info(f"Initial elements: {initial_list}")
        initial_count = len(initial_list)

        #Page Refresh
        self.disappearing_element_page.refresh_page()

        # Get the count of elements after refresh
        present_list = self.disappearing_element_page.elements_text()
        logger.info(f"Elements after refresh: {present_list}")
        present_count = len(present_list)

        # Compare counts and show the difference
        if initial_count != present_count:
            print(f"Element count changed from {initial_count} to {present_count}.")

            missing = set(initial_list) - set(present_list)
            added = set(present_list) - set(initial_list)

            if missing:
                print("❌ Missing elements after refresh:", missing)
            if added:
                print("🆕 New elements after refresh:", added)
        else:
            print("✅ Element count did not change after refresh.")
            assert initial_count == present_count, \
                f"Expected {initial_count} elements, but found {present_count} after refresh."
