import logging
import pytest
from PageObject.LandingPage import LandingPage
import requests

logger = logging.getLogger(__name__)

@pytest.mark.order(2)
@pytest.mark.usefixtures("browser_instance")
class TestBrokenImagePage:
    """
    Test suite for Broken Image Page functionality.
    """
    image_is_rendered = False

    @pytest.fixture(autouse=True)
    def setup(self, request, browser_instance):
        """
        Run before each test — creates fresh LandingPage instance.
        """
        self.driver = browser_instance
        self.landing_page = LandingPage(self.driver)
        self.landing_page.navigate_to_landing_page()
        self.broken_image_page = self.landing_page.go_to_broken_images()

    def test_images_rendering_and_status_code(self):
        """
        Check all images on the page:
        - If rendered → skip HTTP check
        - If NOT rendered → check HTTP status code
        - Collect all failures and report at the end
        """

        images = self.broken_image_page.get_all_images()
        failures = []

        for idx, img in enumerate(images, start=1):
            src = img.get_attribute("src")
            rendered = self.broken_image_page.is_image_rendered(img)
            logger.info(f"rendered : {rendered}")
            if rendered:
                logger.info(f"✅ Image {idx} rendered OK. Src: {src}")
                continue

            logger.warning(f"❌ Image {idx} not rendered. Checking HTTP status for: {src}")
            try:
                response = requests.get(src, timeout=5)
                if response.status_code != 200:
                    failures.append(f"Image {idx} ({src}) - HTTP {response.status_code}")
            except requests.RequestException as e:
                failures.append(f"Image {idx} ({src}) - Request failed: {e}")

        if failures:
            pytest.fail("Some images failed:\n" + "\n".join(failures))
