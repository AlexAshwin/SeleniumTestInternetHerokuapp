import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestGeolocationPage:
    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.geolocation_page = self.landing_page.go_to_geolocation()

    def test_geolocation_page_heading(self):
        """
        Verify the Geolocation page heading.
        """
        expected_heading = "Geolocation"
        actual_heading = self.geolocation_page.get_geolocation_page_heading()
        logger.info(f"Heading found: {actual_heading}")
        assert expected_heading in actual_heading, f"Expected heading to contain '{expected_heading}'"

    def test_current_location(self):
        """
        Verify the current location based on IP.
        """
        ip_location = self.geolocation_page.get_browser_based_location()
        logger.info(f"IP-based location: {ip_location}")

        self.geolocation_page.click_where_am_i_button()
        website_location = self.geolocation_page.fetch_location_from_website()
        logger.info(f"Website location after button click: {website_location}")

        assert abs(ip_location['latitude'] - website_location['latitude']) < 0.1, "Latitude mismatch"
        assert abs(ip_location['longitude'] - website_location['longitude']) < 0.1, "Longitude mismatch"

    def test_send_fake_geolocation(self):
        """
        Verify sending fake geolocation data to the browser.
        """
        fake_latitude = 37.7749
        fake_longitude = -122.4194
        self.geolocation_page.send_fake_geolocation(fake_latitude, fake_longitude)

        self.geolocation_page.click_where_am_i_button()
        website_location = self.geolocation_page.fetch_location_from_website()
        logger.info(f"Website location after sending fake geolocation: {website_location}")

        assert abs(fake_latitude - website_location['latitude']) < 0.1, "Fake latitude mismatch"
        assert abs(fake_longitude - website_location['longitude']) < 0.1, "Fake longitude mismatch"