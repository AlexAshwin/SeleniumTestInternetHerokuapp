import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.order(3)
@pytest.mark.usefixtures("browser_instance")
class TestAddRemoveElementPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.add_remove_element = self.landing_page.go_to_add_remove_elements()

    def test_add_element(self):
        """
        Verify adding an element works correctly.
        """
        initial_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"Initial delete buttons count: {initial_count}")

        self.add_remove_element.add_element()

        new_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"New delete buttons count after adding: {new_count}")

        assert new_count == initial_count + 1, "Element was not added successfully"

    def test_delete_element(self):
        """
        Verify deleting an element works correctly.
        """
        if self.add_remove_element.get_delete_buttons_count() == 0:
            logger.info("No elements to delete, adding one first.")
            self.add_remove_element.add_element()
        initial_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"Initial delete buttons count: {initial_count}")
        self.add_remove_element.delete_element()
        new_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"New delete buttons count after deletion: {new_count}")
        assert new_count == initial_count - 1, "Element was not deleted successfully"



    def test_add_multiple_elements(self):
        """
        Verify adding multiple elements works correctly.
        """
        initial_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"Initial delete buttons count: {initial_count}")
        add_count = self.add_remove_element.get_random_count()
        for _ in range(add_count):
            self.add_remove_element.add_element()
        new_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"New delete buttons count after adding multiple: {new_count}")
        assert new_count == initial_count + add_count, "Multiple elements were not added successfully"

    def test_delete_multiple_elements(self):
        """
        Verify deleting multiple elements works correctly.
        """
        if self.add_remove_element.get_delete_buttons_count() == 0:
            logger.info("No elements to delete, adding some first.")
            add_count = self.add_remove_element.get_random_count()
            for _ in range(add_count):
                self.add_remove_element.add_element()
        initial_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"Initial delete buttons count: {initial_count}")
        delete_count = min(self.add_remove_element.get_random_count(), initial_count)
        logger.info(f"Deleting {delete_count} elements")
        for _ in range(delete_count):
            self.add_remove_element.delete_element()
        new_count = self.add_remove_element.get_delete_buttons_count()
        logger.info(f"New delete buttons count after deleting multiple: {new_count}")
        assert new_count == max(0, initial_count - delete_count), "Multiple elements were not deleted successfully"