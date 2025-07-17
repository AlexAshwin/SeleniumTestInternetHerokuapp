import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestDragAndDropPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.drag_and_drop = self.landing_page.go_to_drag_and_drop()

    def test_drag_and_drop_page_heading(self):
        """
        Verify the heading of the Drag And Drop page.
        """
        logger.info("Testing Drag And Drop page heading")
        expected_heading = "Drag and Drop"
        actual_heading = self.drag_and_drop.get_ab_testing_page_heading()
        assert actual_heading == expected_heading, f"Expected heading '{expected_heading}', but got '{actual_heading}'"

    def test_drag_and_drop_operation(self):
        """
        Verify the drag and drop operation from source box to target box.
        """
        initial_box_text = self.drag_and_drop.get_box_text()
        logger.info(f"Initial box text: {initial_box_text}")
        logger.info("Testing drag and drop operation")
        self.drag_and_drop.drag_and_drop_box()
        actual_box_text = self.drag_and_drop.get_box_text()
        logger.info(f"Box text after drag and drop: {actual_box_text}")
        assert initial_box_text != actual_box_text, "Box text cshould change after drag and drop operation"