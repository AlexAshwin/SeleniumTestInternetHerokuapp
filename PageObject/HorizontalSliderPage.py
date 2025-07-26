from PageObject.BasePage import BasePage


class HorizontalSliderPage(BasePage):
    """
    Page Object for the Geolocation page.
    """
    page_heading = "//h3"
    slider = "input[@type='range']"
    slider_value = "//span[@id='range']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the heading of the Horizontal Slider page.
        :return: The heading text.
        """
        return self.get_text(self.page_heading)

    def get_slider_value(self):
        """
        Get the current value of the horizontal slider.
        :return: The value of the slider as a float.
        """
        slider_value = self.get_text(self.slider_value)
        return float(slider_value)

    def set_slider_value(self, value):
        """
        Set the horizontal slider to a specific value.
        :param value: The value to set the slider to.
        """
        slider = self.enter_text(self.slider, value)



