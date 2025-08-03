import os

from PageObject.BasePage import BasePage


class JqueryUIMenuPage(BasePage):
    """
    Page object for the jQuery UI Menu page.
    """

    page_heading = "//h3"
    menu_locators = {
        "disabled": "//li[@id='ui-id-1']",
        "enabled": "//li[@id='ui-id-3']",
        "downloads": "//li[@id='ui-id-4']",
        "pdf": "//li[@id='ui-id-5']",
        "csv": "//li[@id='ui-id-6']",
        "xls": "//li[@id='ui-id-7']",
        "back to jquery ui": "//li[@id='ui-id-8']",
    }
    should_not_see_text = "//li[@id='ui-id-2']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the heading of the jQuery UI Menu page.

        :return: The heading text.
        """
        return self.get_text(self.page_heading)

    def is_menu_option_enabled(self, option_name: str) -> bool:
        """
        Check if a given menu option is enabled (clickable).

        :param option_name: Name of the menu option (e.g., 'enabled', 'pdf', 'csv')
        :return: True if the menu option is enabled, False otherwise.
        :raises ValueError: If the option_name is invalid.
        """
        key = option_name.casefold()

        if key not in self.menu_locators:
            raise ValueError(f"Invalid menu option name: '{option_name}'")

        xpath = self.menu_locators[key]
        return self.is_element_enabled(xpath)

    def click_menu_option(self, option_name: str):
        """
        Click a menu option by its name.

        :param option_name: Name of the menu option (e.g., 'downloads', 'pdf', 'back')
        :raises ValueError: If the option_name is invalid.
        """
        key = option_name.strip().lower()

        if key not in self.menu_locators:
            raise ValueError(f"Invalid menu option name: '{option_name}'")

        xpath = self.menu_locators[key]
        self.click(xpath)

    def get_download_path(self, request, filename: str):
        """
        Get the full path of the specified downloaded file.

        :param request: Pytest request object (to access download path)
        :param filename: Expected file name (e.g., "some-file.txt")
        :return: Full path to the file if found, else None
        """
        download_dir = getattr(request.node, "_download_path", None)
        if not download_dir:
            return None

        full_path = os.path.join(download_dir, filename)
        return full_path if os.path.exists(full_path) else None