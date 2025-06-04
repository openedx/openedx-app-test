"""
Register Screen Test Module
"""

import pytest
from selenium.webdriver.common.keys import Keys

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_register import IosRegister


@pytest.mark.IOS
class TestIosNewLanding:
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info("Starting Test Case")
        ios_landing = IosLanding()

        if ios_landing.allow_notifications_button.exists(raise_exception=False):
            ios_landing.allow_notifications_button.click()

        logo_image = ios_landing.get_logo_image
        expect(logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
        expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)
        expect(ios_landing.get_search_title).to_have(values.LANDING_SEARCH_TITLE, ElementAttribute.LABEL)

    def test_search_courses_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can search courses, and back to New Landing screen
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_landing = IosLanding()
        search_courses_field = ios_landing.search_courses_field
        search_courses_field.click()
        search_courses_field.send_keys("python")
        search_courses_field.send_keys(Keys.ENTER)
        expect(ios_landing.navigation_bar_title).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME)
        expect(ios_landing.landing_back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)
        expect(ios_landing.go_back_to_landing_screen).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_landing = IosLanding()
        ios_login = IosLogin()
        register_page = IosRegister()

        register_button = ios_landing.register_button
        expect(register_button).to_have(values.REGISTER)
        register_button.click()

        expect(register_page.register_screen_title).to_have(values.REGISTER)
        back_button = ios_landing.back_navigation_button
        expect(back_button).to_have(values.LANDING_BACK_BUTTON)
        assert back_button.click()
        sign_in_button = ios_landing.sign_in_button
        expect(sign_in_button).to_have(values.LOGIN)
        assert sign_in_button.click()
        expect(ios_login.sign_in_title).to_have(values.LOGIN)
        back_button = ios_landing.back_navigation_button
        expect(back_button).to_have(values.LANDING_BACK_BUTTON)
        assert back_button.click()
        expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)
        setup_logging.info("Ending Test Case")
