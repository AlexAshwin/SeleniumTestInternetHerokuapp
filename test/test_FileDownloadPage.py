import logging
import time

import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestExitIntentPage:
    """
    Test suite for Exit Intent page functionalities.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.file_download_page = self.landing_page.go_to_file_download()\

    def test_file_download_page_heading(self):
        """
        Verify the heading of the File Download page.
        """
        expected_heading = "File Download"
        actual_heading = self.file_download_page.get_page_heading()
        logger.info(f"File Download page heading found: {actual_heading}")
        assert expected_heading.casefold() in actual_heading.casefold(), f"Expected heading to contain '{expected_heading}'"

    @pytest.mark.parametrize("filename", ['some-file.txt', 'random_data.txt','cat.jpg'])
    def test_file_download_link(self, request,filename):
        """
        Verify the file download link is present and clickable.
        """
        self.file_download_page.click_file_link(filename)
        time.sleep(10) # Wait for the download to complete
        downloaded_file = self.file_download_page.get_download_path(request,filename)
        assert downloaded_file is not None and downloaded_file.endswith(filename), \
            f"Expected '{filename}' to be downloaded"

        logger.info(f"File downloaded successfully to: {downloaded_file}")