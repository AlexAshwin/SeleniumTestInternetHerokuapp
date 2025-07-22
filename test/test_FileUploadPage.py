import logging
import os

import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("browser_instance")
class TestFileUploadPage:
    """clea
    Test suite for File Upload page functionalities.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.file_upload_page = self.landing_page.go_to_file_upload()

    def test_file_upload_page_heading(self):
        """
        Verify the heading of the File Upload page.
        """
        expected_heading = "File Upload"
        actual_heading = self.file_upload_page.get_page_heading()
        logger.info(f"File Upload page heading found: {actual_heading}")
        assert expected_heading.casefold() in actual_heading.casefold(), f"Expected heading to contain '{expected_heading}'"

    # Dynamically gather files from ./reports/downloads/
    @pytest.mark.parametrize("file_path", [
        os.path.join("Data", "downloads", f)
        for f in os.listdir("Data/downloads")
        if os.path.isfile(os.path.join("Data", "downloads", f))
    ])
    def test_file_upload(self, file_path):
        """
        Verify file upload functionality.
        """
        #converts the relative file path to an absolute path
        abs_path = os.path.abspath(file_path)
        logger.info(f"Uploading file: {abs_path}")
        #sending the absolute path to the file upload input
        self.file_upload_page.upload_file(abs_path)
        # Click the upload button to submit the file
        self.file_upload_page.click_upload_button()
        # Add assertions or checks to verify successful upload if applicable
        message, uploaded_file_name = self.file_upload_page.is_file_uploaded()
        assert message == "File Uploaded!" and uploaded_file_name == os.path.basename(file_path), \
            f"Expected file upload confirmation but got '{message}' with file '{uploaded_file_name}'"
        logger.info(f"File '{file_path}' uploaded successfully.")