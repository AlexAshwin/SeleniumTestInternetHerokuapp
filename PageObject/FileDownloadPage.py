from PageObject.BasePage import BasePage
import os

class FileDownloadPage(BasePage):

    # XPath locators for elements on the File Download page
    heading = "//h3"
    file_link_template = "//a[@href='download/{filename}']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_heading(self):
        """
        Get the title of the File Download page.

        :return: Title of the File Download page.
        """
        return self.get_text(self.heading)

    def click_file_link(self,filename:str):
        """
        Click the file download link to initiate the download.

        :return: None
        """
        file_xpath = self.file_link_template.format(filename=filename)
        self.click(file_xpath)

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
