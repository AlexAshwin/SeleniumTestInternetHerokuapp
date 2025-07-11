from PageObject.BasePage import BasePage


class DragAndDropPage(BasePage):

    #XPath locators for elements on the AB Testing page
    heading = "//h3"
    source_box = "//div[@id='column-a']"
    target_box = "//div[@id='column-b']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_ab_testing_page_heading(self):
        """
        Get the title of the Drag And Drop page.

        :return: Title of the Drag And Drop page.
        """
        return self.get_text(self.heading)

    def drag_and_drop_box(self):
        """
        Perform drag and drop operation from source box to target box.
        """
        self.drag_and_drop(self.source_box, self.target_box)

    def get_box_text(self):
        """
        Get the text of the target box after drag and drop operation.

        :return: list of text in box.
        """
        source_text = self.get_text(self.source_box)
        target_text = self.get_text(self.target_box)
        return source_text, target_text