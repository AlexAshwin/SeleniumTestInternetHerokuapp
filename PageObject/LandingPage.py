from PageObject.BasePage import BasePage
import pytest

from PageObject.DigestAuthPage import DigestAuthPage


class LandingPage(BasePage):
    """
    Page object for the application's landing page.
    Inherits common Selenium operations from BasePage.
    """

    # Example XPath locators for elements on the landing page
    heading = "//h1[@class='heading']"
    abtesting = "//a[@href='/abtest']"
    add_remove_elements = "//a[@href='/add_remove_elements/']"
    broken_image = "//a[@href='/broken_images']"
    challenging_dom = "//a[@href='/challenging_dom']"
    checkboxes = "//a[@href='/checkboxes']"
    context_menu = "//a[@href='/context_menu']"
    digest_auth = "//a[@href='/digest_auth']"
    disappearing_elements = "//a[@href='/disappearing_elements']"
    drag_and_drop = "//a[@href='/drag_and_drop']"
    dropdown = "//a[@href='/dropdown']"
    dynamic_content = "//a[@href='/dynamic_content']"
    dynamic_control = "//a[@href='/dynamic_controls']"
    dynamic_loading = "//a[@href='/dynamic_loading']"
    entry_ad = "//a[@href='/entry_ad']"
    exit_intent = "//a[@href='/exit_intent']"

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
        self.click(self.broken_image)
        return BrokenImagePage(self.driver)

    def go_to_challenging_dom(self):
        """
        Navigate to the Challenging DOM page.
        :return: ChallengingDOMPage object.
        """
        from PageObject.ChallengingDomPage import ChallengingDomPage
        self.click(self.challenging_dom)
        return ChallengingDomPage(self.driver)

    def go_to_checkboxes(self):
        """
        Navigate to the Checkboxes page.
        :return: CheckboxesPage object.
        """
        from PageObject.CheckboxesPage import CheckboxesPage
        self.click(self.checkboxes)
        return CheckboxesPage(self.driver)

    def go_to_context_menu(self):
        """
        Navigate to the Context Menu page.
        :return: ContextMenuPage object.
        """
        from PageObject.ContextMenuPage import ContextMenuPage
        self.click(self.context_menu)
        return ContextMenuPage(self.driver)

    def go_to_digest_auth(self,username, password):
        """
        Navigate to the Basic Authentication page with provided credentials.
        :param username:
        :param password:
        :return:
        """
        from PageObject.DigestAuthPage import DigestAuthPage
        # Inject credentials into the link using JavaScript
        self.driver.execute_script(f'''
            const link = document.querySelector("a[href='/digest_auth']");
            if (link) {{
                link.href = "https://{username}:{password}@the-internet.herokuapp.com/digest_auth";
            }}
        ''')

        # Click the modified link
        self.click(f"//a[@href='https://{username}:{password}@the-internet.herokuapp.com/digest_auth']")

        return DigestAuthPage(self.driver)

    def go_to_disappearing_elements(self):
        """
        Navigate to the Disappearing Elements page.
        :return: DisappearingElementsPage object.
        """
        from PageObject.DisappearingElementsPage import DisappearingElementsPage
        self.click(self.disappearing_elements)
        return DisappearingElementsPage(self.driver)

    def go_to_drag_and_drop(self):
        """
        Navigate to the Drag and Drop page.
        :return: DragAndDropPage object.
        """
        from PageObject.DragAndDropPage import DragAndDropPage
        self.click(self.drag_and_drop)
        return DragAndDropPage(self.driver)

    def go_to_dropdown(self):
        """
        Navigate to the Dropdown page.
        :return: DropdownPage object.
        """
        from PageObject.DropdownPage import DropdownPage
        self.click(self.dropdown)
        return DropdownPage(self.driver)

    def go_to_dynamic_content(self):
        """
        Navigate to the Dynamic Content page.
        :return: DynamicContentPage object.
        """
        from PageObject.DynamicContentPage import DynamicContentPage
        self.click(self.dynamic_content)
        return DynamicContentPage(self.driver)

    def go_to_dynamic_control(self):
        """
        Navigate to the Dynamic Control page.
        :return: DynamicControlPage object.
        """
        from PageObject.DynamicControlPage import DynamicControlPage
        self.click(self.dynamic_control)
        return DynamicControlPage(self.driver)

    def go_to_dynamic_loading(self):
        """
        Navigate to the Dynamic Loading page.
        :return: DynamicLoadingPage object.
        """
        from PageObject.DynamicLoadingPage import DynamicLoadingPage
        self.click(self.dynamic_loading)
        return DynamicLoadingPage(self.driver)

    def go_to_entry_ad(self):
        """
        Navigate to the Entry Ad page.
        :return: EntryAdPage object.
        """
        from PageObject.EntryAdPage import EntryAdPage
        self.click(self.entry_ad)
        return EntryAdPage(self.driver)

    def go_to_exit_intent(self):
        """
        Navigate to the Exit Intent page.
        :return: ExitIntentPage object.
        """
        from PageObject.ExitIntentPage import ExitIntentPage
        self.click(self.exit_intent)
        return ExitIntentPage(self.driver)
