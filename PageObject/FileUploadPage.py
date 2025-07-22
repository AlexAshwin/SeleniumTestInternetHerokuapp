from PageObject.BasePage import BasePage

class FileUploadPage(BasePage):
    """
    FileUploadPage encapsulates operations for the File Upload page.
    """

    # XPath locators for elements on the File Upload page.
    heading = "//h3"
    file_input = "//input[@type='file']"
    upload_button = "//input[@value='Upload']"
    uploaded_file = "//div[@id='uploaded-files']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the title of the File Upload page.

        :return: Title of the File Upload page.
        """
        return self.get_text(self.heading)

    def upload_file(self, file_path: str):
        """
        Upload a file using the file input element.

        :param file_path: Full path to the file to be uploaded.
        """
        self.enter_text(self.file_input, file_path)

    def click_upload_button(self):
        """
        Click the upload button to submit the file.
        """
        self.click(self.upload_button)

    def is_file_uploaded(self):
        """
        Check if the file is successfully uploaded.

        :param file_name: Name of the file to check.
        :return: True if the file is uploaded, False otherwise.
        """
        # This method can be extended to check for a success message or confirmation
        message = self.get_text(self.heading)
        file_name = self.get_text(self.uploaded_file)
        return message,file_name