from PageObject.BasePage import BasePage


class FloatingMenuPage(BasePage):
    # XPath locators for elements on the Floating Menu Page
    heading = "//h3"
    menu_xpath = "//div[@id='menu']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the main heading of the Floating Menu page.
        :return: Main heading text.
        """
        return self.get_text(self.heading)

    def is_menu_visible(self) -> bool:
        """
        Check if the floating menu is currently visible.
        :return: True if the menu is visible, False otherwise.
        """
        return self.is_element_visible(self.menu_xpath)

    def get_menu_items(self):
        """
        Get the list of menu items in the floating menu.
        :return: List of menu item texts.
        """
        menu_items = self.find_elements(f"{self.menu_xpath}//a")
        return [item.text.strip() for item in menu_items if item.text.strip()]

    def scroll_to_middle_of_page(self):
        """
        Scroll to the middle of the page to ensure the floating menu is visible.
        """
        self.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")

    def scroll_to_end_of_page(self):
        """
        Scroll to the end of the page to ensure the floating menu is visible.
        """
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top_of_page(self):
        """
        Scroll to the top of the page to ensure the floating menu is visible.
        """
        self.execute_script("window.scrollTo(0, 0);")