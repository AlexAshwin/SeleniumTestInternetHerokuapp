import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestHorizontalSliderPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.horizontal_slider_page = self.landing_page.go_to_horizontal_slider()

    def test_horizontal_slider_page_heading(self):
        """
        Verify the Horizontal Slider page heading.
        """
        expected_heading = "Horizontal Slider"
        actual_heading = self.horizontal_slider_page.get_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_slider_value(self):
        """
        Verify the initial value of the horizontal slider.
        """
        initial_value = self.horizontal_slider_page.get_slider_value()
        logger.info(f"Initial slider value: {initial_value}")
        assert initial_value == 0.0, "Initial slider value should be 0.0"

    @pytest.mark.parametrize("target_value", [i * 0.5 for i in range(11)])
    def test_set_slider_value(self,target_value):
        """
        Set the horizontal slider to a specific value and verify it.
        """
        self.horizontal_slider_page.set_slider_value(target_value)    # since step=0.5

        current_value = self.horizontal_slider_page.get_slider_value()
        logger.info(f"Slider value after setting: {current_value}")

        assert current_value == target_value, f"Expected slider value to be {target_value}, but got {current_value}"

