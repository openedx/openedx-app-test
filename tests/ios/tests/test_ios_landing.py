"""
    Register Screen Test Module
"""

from selenium.webdriver.common.keys import Keys

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin


class TestIosNewLanding():
    """
    New Landing screen's Test Case
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
        back_button = ios_landing.get_back_button()
        assert back_button.get_attribute('label') == values.BACK_BUTTON
        assert ios_landing.load_landing_screen().text == values.LANDING_LOGO_IMAGE

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping "Sign in" will load "Sign In" screen
            Verify tapping back/cross icon from 'Sign In' screen navigate user
                back to 'New Landing' screen
            Verify tapping "Register" loads "Register" screen
            Verify tapping back/cross icon from "Register" screen
                navigate user back to 'New Landing' screen
        """

        ios_landing = IosLanding(set_capabilities, setup_logging)
        ios_login = IosLogin(set_capabilities, setup_logging)

        register_button = ios_landing.get_register_button()
        assert register_button.text == values.REGISTER
        register_button.click()

        register_title = ios_landing.get_register_screen_title()
        assert register_title.text == values.REGISTER
        back_button = ios_landing.get_header_back_button()
        assert back_button.text == values.LANDING_BACK_BUTTON
        back_button.click()

        signin_button = ios_landing.get_sign_in_button()
        assert signin_button.text == values.LOGIN
        signin_button.click()

        sign_in_title = ios_login.get_sign_in_title()
        assert sign_in_title.text == values.LOGIN
        back_button = ios_landing.get_header_back_button()
        assert back_button.text == values.LANDING_BACK_BUTTON
        back_button.click()

        welcome_message = ios_landing.get_welcome_message()
        assert welcome_message.text == values.LANDING_MESSAGE_IOS
        setup_logging.info('Ending Test Case')
