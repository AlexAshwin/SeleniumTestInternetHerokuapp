import json
import logging
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

# Load test credentials
test_data_path = './Data/credentials.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    cred_list = test_data['data']['form_auth_credentials']


@pytest.mark.usefixtures("browser_instance")
class TestFormAuthenticationPage:
    """
    Test class for Form Authentication Page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.form_authentication_page = self.landing_page.go_to_form_authentication()

    def test_form_authentication_page_heading(self):
        """
        Verify the heading of the Form Authentication page.
        """
        expected_heading = "Login Page"
        actual_heading = self.form_authentication_page.get_page_heading()
        logger.info(f"Form Authentication page heading found: {actual_heading}")
        assert expected_heading.casefold() in actual_heading.casefold(), f"Expected heading to contain '{expected_heading}'"

    @pytest.mark.parametrize("test_case", cred_list['invalid'])
    def test_form_authentication_invalid_login(self, test_case):
        """
        Verify invalid login functionality.
        """
        username = test_case['username']
        password = test_case['password']

        logger.info(f"Testing invalid login with username: {username} and password: {password}")

        self.form_authentication_page.enter_username(username)
        self.form_authentication_page.enter_password(password)
        self.form_authentication_page.click_login()
        message = self.form_authentication_page.get_message()
        logger.info(f"Message found after invalid login: {message}")
        assert (
                "Your username is invalid!" in message or
                "Your password is invalid!" in message
        ), f"Unexpected error message: {message}"

    @pytest.mark.parametrize("test_case", cred_list['valid'])
    def test_form_authentication_valid_login(self, test_case):
        """
        Verify valid login functionality.
        """
        username = test_case['username']
        password = test_case['password']

        logger.info(f"Testing valid login with username: {username} and password: {password}")

        self.form_authentication_page.enter_username(username)
        self.form_authentication_page.enter_password(password)
        self.form_authentication_page.click_login()
        message = self.form_authentication_page.get_message()
        logger.info(f"Message found after valid login: {message}")
        assert "You logged into a secure area!" in message, "Login failed for valid credentials"

    @pytest.mark.parametrize("test_case", cred_list['valid'])
    def test_logout_functionality(self,test_case):
        """
        Verify logout functionality.
        """
        # Assuming the valid credentials are used for login
        username = test_case['username']
        password = test_case['password']
        logger.info(f"Testing valid login with username: {username} and password: {password}")
        self.form_authentication_page.enter_username(username)
        self.form_authentication_page.enter_password(password)
        self.form_authentication_page.click_login()
        # Now perform logout
        self.form_authentication_page.click_logout()
        message = self.form_authentication_page.get_message()
        assert "You logged out of the secure area!" in message, "Logout failed or message not as expected"