import time

from PageObject.BasePage import BasePage
import requests

class GeolocationPage(BasePage):
    """
    Page Object for the Geolocation page.
    """
    geolocation_page_heading = "//h3"
    where_am_i_button = "//button[contains(text(),'Where am I?')]"
    latitude_text = "//div[@id='lat-value']"
    longitude_text = "//div[@id='long-value']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_geolocation_page_heading(self):
        """
        Get the heading of the Geolocation page.
        :return: The heading text.
        """
        return self.get_text(self.geolocation_page_heading)

    def click_where_am_i_button(self):
        """
        Click the 'Where Am I?' button to get the geolocation.
        """

        self.click(self.where_am_i_button)

    def get_browser_based_location(self, timeout: int = 10):
        """
        Use browser's navigator.geolocation to get current location.
        Requires user to allow location access or a mocked location to be set.

        :param timeout: Time in seconds to wait for geolocation result.
        :return: Dict with latitude and longitude.
        """

        # JS to asynchronously get geolocation and store it in window._geo
        js_script = """
        window._geo = null;
        navigator.geolocation.getCurrentPosition(function(pos) {
            window._geo = {
                latitude: pos.coords.latitude,
                longitude: pos.coords.longitude
            };
        });
        """
        self.driver.execute_script(js_script)

        # Wait and retrieve the result
        for _ in range(timeout * 5):  # check every 0.1 sec
            geo = self.driver.execute_script("return window._geo;")
            if geo:
                return geo
            time.sleep(0.1)

        raise TimeoutError("Failed to retrieve browser geolocation within timeout.")

    def fetch_location_from_website(self):
        """
        Fetch the geolocation from the website after clicking the button.
        :return: A dictionary containing latitude and longitude.
        """
        latitude = self.get_text(self.latitude_text)
        longitude = self.get_text(self.longitude_text)
        return {
            'latitude': float(latitude),
            'longitude': float(longitude)
        }

    def send_fake_geolocation(self, latitude, longitude):
        """
        Send fake geolocation data to the browser.
        :param latitude: Latitude to set.
        :param longitude: Longitude to set.
        """
        self.driver.execute_script(f"window.navigator.geolocation.getCurrentPosition = function(success) {{"
                                   f"success({{ coords: {{ latitude: {latitude}, longitude: {longitude} }} }});"
                                   f"}}")
