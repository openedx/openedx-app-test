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
        assert search_courses_field.text == values.LANDING_SEARCH_COURSES
        search_courses_field.send_keys('python')
        search_courses_field.send_keys(Keys.ENTER)
        disocvery_title = global_contents.get_ios_all_static_text(set_capabilities)[0]
        assert disocvery_title.text == values.DISCOVER_SCREEN_HEADING

        back_button =  global_contents.get_ios_all_buttons(set_capabilities)[0]
        assert back_button.text == values.BACK_BUTTON
        back_button.click()

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
        global_contents = Globals(setup_logging)
        all_buttons = global_contents.get_ios_all_buttons(set_capabilities)

        register_button = all_buttons[1]
        assert register_button.text == values.REGISTER
        register_button.click()

        all_static_text = global_contents.get_ios_all_static_text(set_capabilities)
        sign_up_heading = all_static_text[1]
        assert sign_up_heading.text == values.REGISTER_SIGN_UP_HEADING

        back_button =  global_contents.get_ios_all_buttons(set_capabilities)[0]
        assert back_button.text == 'arrowLeft'
        back_button.click()

        signin_button =  ios_login.get_sign_in_button()
        assert signin_button.text == values.LOGIN
        signin_button.click()

        sign_in_heading = global_contents.get_ios_all_static_text(set_capabilities)[0]
        assert sign_in_heading.text == values.LOGIN
        back_button =  global_contents.get_ios_all_buttons(set_capabilities)[0]
        assert back_button.text == 'arrowLeft'
        back_button.click()

        welcome_message = ios_landing.get_welcome_message()
        assert welcome_message.text == values.LANDING_MESSAGE_IOS
        setup_logging.info('Ending Test Case')
