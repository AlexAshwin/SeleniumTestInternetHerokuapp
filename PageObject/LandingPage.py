from PageObject.BasePage import BasePage
import pytest


class LandingPage(BasePage):
    """
    Page object for the application's landing page.
    Inherits common Selenium operations from BasePage.
    """

    # Example XPath locators for elements on the landing page
    heading = "//h1[@class='heading']"
    abtesting = "//a[@href='/abtest']"

    add_remove_elements = "//a[@href='/add_remove_elements/']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/"

    def navigate_to_landing_page(self):
        """
        Navigate to the landing page URL.
        """
        self.open(self.url)

    def get_landing_page_title(self):
        """
        Get the title of the landing page.

        :return: Title of the landing page.
        """
        return self.get_title()

    def get_page_heading(self):
        """
        Get the main heading of the landing page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

    def go_to_ab_testing(self):
        """
        Navigate to the AB Testing page.
        :return: ABTestingPage object.
        """
        from PageObject.ABTestingPage import ABTestingPage
        self.click(self.abtesting)
        return ABTestingPage(self.driver)

    def go_to_add_remove_elements(self):
        """
        Navigate to the Add/Remove Elements page.
        :return: AddRemoveElementsPage object.
        """
        self.click(self.add_remove_elements)
        from PageObject.AddRemoveElementPage import AddRemoveElementPage
        return AddRemoveElementPage(self.driver)


    def go_to_basic_auth(self,username, password):
        """
        Navigate to the Basic Authentication page with provided credentials.
        :param username:
        :param password:
        :return:
        """
        from PageObject.BasicAuthPage import BasicAuthPage
        # Inject credentials into the link using JavaScript
        self.driver.execute_script(f'''
            const link = document.querySelector("a[href='/basic_auth']");
            if (link) {{
                link.href = "https://{username}:{password}@the-internet.herokuapp.com/basic_auth";
            }}
        ''')

        # Click the modified link
        self.click(f"//a[@href='https://{username}:{password}@the-internet.herokuapp.com/basic_auth']")

        return BasicAuthPage(self.driver)

    def go_to_broken_images(self):
        """
        Navigate to the Broken Images page.
        :return: BrokenImagesPage object.
        """
        from PageObject.BrokenImagePage import BrokenImagePage
        self.click("//a[@href='/broken_images']")
        return BrokenImagePage(self.driver)
