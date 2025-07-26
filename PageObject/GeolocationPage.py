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

    def get_ip_based_location(self):
        """
        Fetch approximate location based on IP (not browser geolocation).
        """
        response = requests.get('https://ipinfo.io/json')
        if response.status_code == 200:
            data = response.json()
            lat, lon = data.get('loc').split(',')
            return {'latitude': float(lat), 'longitude': float(lon)}
        else:
            raise Exception("Failed to retrieve geolocation data from IP")

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