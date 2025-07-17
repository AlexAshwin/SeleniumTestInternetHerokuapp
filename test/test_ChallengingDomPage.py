import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestChallengingDomPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.challenging_dom = self.landing_page.go_to_challenging_dom()


    def test_button1_click(self):
        """
        Test clicking the first button on the Challenging DOM page.
        """
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info("Testing click on Button 1")
        logger.info(f"Taking initial canvas image hash before clicking Button 1")
        img_before_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Initial canvas image hash: {img_before_h64}")
        logger.info("Clicking Button 1")
        self.challenging_dom.click_button1()
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info(f"Taking canvas image hash after clicking Button 1")
        img_after_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Canvas image hash after clicking Button 1: {img_after_h64}")
        assert img_before_h64 != img_after_h64, "Canvas image hash should change after clicking Button 1"

    def test_button2_click(self):
        """
        Test clicking the second button on the Challenging DOM page.
        """
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info("Testing click on Button 2")
        logger.info(f"Taking initial canvas image hash before clicking Button 2")
        img_before_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Initial canvas image hash: {img_before_h64}")
        logger.info("Clicking Button 2")
        self.challenging_dom.click_button2()
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info(f"Taking canvas image hash after clicking Button 2")
        img_after_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Canvas image hash after clicking Button 2: {img_after_h64}")
        assert img_before_h64 != img_after_h64, "Canvas image hash should change after clicking Button 2"

    def test_button3_click(self):
        """
        Test clicking the third button on the Challenging DOM page.
        """
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info("Testing click on Button 3")
        logger.info(f"Taking initial canvas image hash before clicking Button 3")
        img_before_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Initial canvas image hash: {img_before_h64}")
        logger.info("Clicking Button 3")
        self.challenging_dom.click_button3()
        logger.info("Verifying Challenging DOM page is loaded")
        assert self.challenging_dom.get_heading() == "Challenging DOM", \
            "Challenging DOM page heading should be 'Challenging DOM'"
        logger.info(f"Taking canvas image hash after clicking Button 3")
        img_after_h64 = self.challenging_dom.get_canvas_image()
        logger.info(f"Canvas image hash after clicking Button 3: {img_after_h64}")
        assert img_before_h64 != img_after_h64, "Canvas image hash should change after clicking Button 3"

