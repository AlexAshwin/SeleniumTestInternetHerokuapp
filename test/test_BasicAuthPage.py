import logging
import json
import pytest
from PageObject.LandingPage import LandingPage

logger = logging.getLogger(__name__)

# Load test credentials
test_data_path = './Data/credentials.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    cred_list = test_data['data']['basic_auth_credentials']

@pytest.mark.order(3)
@pytest.mark.usefixtures("browser_instance")
class TestAddRemoveElementPage:

    @pytest.mark.parametrize("test_case", cred_list)
    @pytest.fixture(autouse=True)
    def setup(self, browser_instance, test_case):
        """
        Run before each test — setup browser and navigate using credentials.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()

        # Use test_case (injected from parametrize) here
        username = test_case['username']
        password = test_case['password']

        self.basic_auth_page = self.landing_page.go_to_basic_auth(username=username, password=password)

    @pytest.mark.parametrize("test_case", cred_list)
    def test_basic_auth(self, test_case):
        """
        Verify basic authentication works correctly.
        """
        logger.info(f"Testing Basic Auth with credentials: {test_case}")
        message = self.basic_auth_page.get_page_heading()
        logger.info(f"Message found: {message}")
        assert "Congratulations" in message, f"Login failed for: {test_case}"
