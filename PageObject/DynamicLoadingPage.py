from PageObject.BasePage import BasePage


class DynamicLoadingPage(BasePage):
    """
    DynamicLoadingPage encapsulates operations for the Dynamic Loading page.
    """

    # XPath locators for elements on the Dynamic Loading page.
    heading = "//h3"
    example1_link = "//a[@href='/dynamic_loading/1']"
    example2_link = "//a[@href='/dynamic_loading/2']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the title of the Dynamic Loading page.

        :return: Title of the Dynamic Loading page.
        """
        return self.get_text(self.heading)

    def go_to_example1(self):
        """
        Navigate to Example 1 of Dynamic Loading.
        :return: DynamicLoadingExample1Page object.
        """
        self.click(self.example1_link)
        return DynamicLoadingExample1Page(self.driver)

    def go_to_example2(self):
        """
        Navigate to Example 2 of Dynamic Loading.
        :return: DynamicLoadingExample2Page object.
        """
        self.click(self.example2_link)
        return DynamicLoadingExample2Page(self.driver)

class DynamicLoadingExample1Page(BasePage):
    """
    DynamicLoadingExample1Page encapsulates operations for the Example 1 of Dynamic Loading page.
    """

    # XPath locators for elements on the Example 1 page.
    start_button = "//button[contains(text(),'Start')]"
    loading_message = "//div[@id='loading']"
    message = "//div[@id='finish']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_message_visible(self):
        """
        Check if the loading message is visible on the page.
        :return: True if the loading message is visible, False otherwise.
        """
        return self.is_element_visible(self.message)


    def click_start_button(self):
        """
        Click the start button to initiate loading.
        """
        self.click(self.start_button)
        self.wait_for_element_to_disappear(self.loading_message)

class DynamicLoadingExample2Page(BasePage):
    """
    DynamicLoadingExample2Page encapsulates operations for the Example 2 of Dynamic Loading page.
    """

    # XPath locators for elements on the Example 2 page.
    start_button = "//button[contains(text(),'Start')]"
    loading_message = "//div[@id='loading']"
    message = "//div[@id='finish']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_message_visible(self):
        """
        Check if the loading message is visible on the page.

        :return: True if the loading message is visible, False otherwise.
        """
        return self.is_element_visible(self.message)

    def click_start_button(self):
        """
        Click the start button to initiate loading.
        """
        self.click(self.start_button)
        self.wait_for_element_to_disappear(self.loading_message)