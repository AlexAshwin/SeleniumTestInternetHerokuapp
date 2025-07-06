

class ChallengingDomPage(BasePage):
    """
    Page Object for the Challenging DOM page.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def get_heading(self):
        """
        Get the heading text of the Challenging DOM page.
        :return: Heading text.
        """
        return self.get_text(self.heading)