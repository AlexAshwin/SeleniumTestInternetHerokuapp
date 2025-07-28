from PageObject.BasePage import BasePage


class HorizontalSliderPage(BasePage):
    """
    Page Object for the Geolocation page.
    """
    page_heading = "//h3"
    slider = "//input[@type='range']"
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

    def set_slider_value(self, target_value):
        """
        Set the horizontal slider to a specific value using pixel offset.
        """
        min_value = 0.0
        max_value = 5.0
        step = 0.5

        slider = self.find_element(self.slider)
        slider_width = slider.size['width']  # Example: 129px

        # Total number of steps
        total_steps = (max_value - min_value) / step  # 10 steps (0.0 to 5.0, by 0.5)
        # Pixel per step
        pixels_per_step = int(slider_width / total_steps)  # e.g. 129/10 = 12.9px

        # Slider starts at 2.5 by default (center), so calculate steps from there
        current_value = 2.5
        steps_to_move = int((target_value - current_value) / step)
        pixel_offset = int(steps_to_move * pixels_per_step)

        self.move_slider(slider, pixel_offset)


