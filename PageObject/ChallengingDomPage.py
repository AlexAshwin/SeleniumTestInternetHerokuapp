from PageObject.BasePage import BasePage
import hashlib
import base64


class ChallengingDomPage(BasePage):
    """
    Page Object for the Challenging DOM page.
    """
    heading = "//h3"
    button1 = "//a[@class='button']"
    button2 = "//a[@class='button alert']"
    button3 = "//a[@class='button success']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_heading(self):
        """
        Get the heading text of the Challenging DOM page.
        :return: Heading text.
        """
        return self.get_text(self.heading)

    def click_button1(self):
        """
        Click on the first button.
        """
        self.click(self.button1)

    def click_button2(self):
        """
        Click on the second button.
        """
        self.click(self.button2)

    def click_button3(self):
        """
        Click on the third button.
        """
        self.click(self.button3)

    def get_canvas_image(self):
        """
        Retrieves the canvas image as a base64-encoded PNG from the web page using JavaScript,
        decodes it, and returns its SHA-256 hash. Useful for verifying if the canvas content has changed.
        :return: SHA-256 hash of the canvas image.
        """
        get_canvas_base64 = """const canvas = document.querySelector("canvas");
        return canvas.toDataURL("image/png").split(",")[1];  // base64 string
        """
        img_b64 = self.execute_script(get_canvas_base64)
        return hashlib.sha256(base64.b64decode(img_b64)).hexdigest()
