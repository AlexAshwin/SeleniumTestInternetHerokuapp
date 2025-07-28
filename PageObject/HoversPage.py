from PageObject.BasePage import BasePage

class HoversPage(BasePage):
    """
    Page object for the Hovers page.
    """
    page_heading= "//h3"
    user = "(//div[@class='figure']//img)"
    hover_text = "(//div[@class='figcaption']//h5)"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the heading of the Hovers page.
        :return: The heading text.
        """
        return self.get_text(self.page_heading)

    def list_of_users(self):
        """
        Get the list of user images on the Hovers page.

        :return: List of user image elements.
        """
        return len(self.find_elements(self.user))

    def hover_over_user(self, user_number):
        """
        Hover over a user image to reveal the user information.

        :param user_number: 1, 2, or 3 to specify which user to hover over.
        :return: The text revealed after hovering over the user.
        """
        user_xpath = f"{self.user}[{user_number}]"
        self.hover(user_xpath)
        return self.get_text(f"{self.hover_text}[{user_number}]")
