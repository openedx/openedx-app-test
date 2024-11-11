"""
    Discovery Screen Test Module
"""

from selenium.webdriver.common.keys import Keys

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin


class TestIosDiscovery():
    """
    Discovery screen's Test Case
    """

    def test_start_new_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Landing screen is loaded successfully
            Verify following contents are visible on screen, 
                "edX logo", "Message" text-field, "Search Courses" edit-field,
                "Register" button, "Sign In" button
            Verify all contents have their default values
        """

        setup_logging.info('Starting Test Case')
        ios_landing = IosLanding(set_capabilities, setup_logging)

        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()

        logo_image = ios_landing.get_logo_image()
        assert logo_image.text == values.LANDING_LOGO_IMAGE

        welcome_message = ios_landing.get_welcome_message()
        assert welcome_message.text == values.LANDING_MESSAGE_IOS

        search_title = ios_landing.get_search_title()
        assert search_title.text == values.LANDING_SEARCH_TITLE

    def test_search_courses_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can search courses, and back to New Landing screen
        """

        ios_landing = IosLanding(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        search_courses_field = ios_landing.get_search_courses_field()
        assert search_courses_field
        search_courses_field.send_keys('python')
        search_courses_field.send_keys(Keys.ENTER)

        disocvery_title = global_contents.get_navigation_bar_title(set_capabilities)[0]
        assert disocvery_title.get_attribute('name') == values.DISCOVER_SCREEN_HEADING
