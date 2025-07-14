import hashlib

import requests
from selenium.webdriver.common.by import By

from PageObject.BasePage import BasePage


class DynamicContentPage(BasePage):
    """
    Dynamic Content Page Object.
    This page contains dynamic content that changes on each visit.
    """
    #XPaths for elements on the Dynamic Content page
    heading = "//h3"
    content_row= "//div[@class='example']//div[@id='content']//div[@class='row']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the heading of the Dynamic Content page.
        :return: The text of the page heading.
        """
        return self.get_text(self.heading)

    def get_dynamic_content(self):
        """
        Get the dynamic content displayed on the page.
        :return: The text of the dynamic content.
        """
        content = {}

        rows = self.find_elements(self.content_row)  # e.g., content_row = (By.CLASS_NAME, "row")

        for index, row in enumerate(rows):
            # Get the image src and calculate hash
            img_element = row.find_element(By.TAG_NAME, "img")
            img_url = img_element.get_attribute("src")

            # Download the image content and hash it
            img_response = requests.get(img_url)
            img_hash = hashlib.md5(img_response.content).hexdigest()

            # Get the text content from the row (usually inside a div with class "large-10 columns")
            text_element = row.find_element(By.CLASS_NAME, "large-10")
            text = text_element.text.strip()

            # Store in dict
            content[f"row_{index + 1}"] = {
                "image": img_hash,
                "text": text
            }

        return content