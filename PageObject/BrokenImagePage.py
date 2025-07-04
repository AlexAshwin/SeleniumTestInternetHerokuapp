import logging

import requests

from PageObject.BasePage import BasePage

logger = logging.getLogger(__name__)

class BrokenImagePage(BasePage):

    #XPath locators for elements on the AB Testing page
    image_xpath = "//div[@class='example']//img"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_image_rendered(self, image):
        """
        Check if an image is rendered on the page.

        :param image_xpath: XPath of the image element.
        :return: True if the image is rendered, False otherwise.
        """
        try:
            return image.is_displayed() and image.get_attribute("naturalWidth") != "0"
        except Exception as e:
            return False

    def get_all_images(self):
        """
        Get all image elements on the page.

        :return: List of image elements.
        """
        return self.find_elements(self.image_xpath)

