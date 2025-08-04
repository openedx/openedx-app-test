"""Landing Screen Test Module"""

import pytest
import allure
from selenium.webdriver.common.keys import Keys

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_register import IosRegister


@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestIosSmokeLandingScreen:
    """Landing screen's Test Case"""

    def test_ios_smoke_landing_screen(self, set_capabilities, setup_logging):
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
        ios_discover_page = IosDiscoverPage()
        ios_login = IosLogin()
        register_page = IosRegister()

        if ios_landing.allow_notifications_button.exists(raise_exception=False):
            ios_landing.allow_notifications_button.click()

        with allure.step("Verify New Landing screen is loaded successfully"):
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)
            expect(ios_landing.get_search_title).to_have(values.LANDING_SEARCH_TITLE, ElementAttribute.LABEL)
            expect(ios_landing.register_button).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(ios_landing.sign_in_button).to_have(values.LOGIN, ElementAttribute.LABEL)
            expect(ios_landing.register_button).to_be_enabled()
            expect(ios_landing.sign_in_button).to_be_enabled()
            expect(ios_landing.explore_all_courses_button).to_have(
                values.LANDING_EXLPORE_COURSES, ElementAttribute.LABEL
            )
            expect(ios_landing.search_magnifying_glass_icon).to_have(values.LANDING_SEARCH_ICON, ElementAttribute.LABEL)

        with allure.step("Click on search courses field"):
            search_courses_field = ios_landing.search_courses_field
            search_courses_field.click()
            search_courses_field.send_keys(values.DISCOVERY_TRENDING_COURSE_PYTHON)
            search_courses_field.send_keys(Keys.ENTER)

        with allure.step("Verify search results are displayed"):
            expect(ios_landing.navigation_bar_title).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME)
            expect(ios_discover_page.all_filters_dropdown).to_exist()

            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.search_field).to_have(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.VALUE
            )
            expect(ios_discover_page.results_for_text).to_contain(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.LABEL
            )
            expect(ios_discover_page.back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)

        with allure.step("Click on back button to return to landing page"):
            ios_discover_page.back_button.click()
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.all_filters_dropdown).to_exist()
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.find_by_text_on_screen(values.DISCOVER_SCREEN_HEADING_PART1)).to_exist()
            expect(ios_discover_page.find_by_text_on_screen(values.DISCOVER_SCREEN_HEADING_PART2)).to_exist()
            expect(ios_discover_page.search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, ElementAttribute.VALUE)
            expect(ios_discover_page.search_button).to_have(values.DISCOVERY_SEARCH_BUTTON, ElementAttribute.LABEL)

        with allure.step("Click on back button to return to landing page"):
            ios_discover_page.back_button.click()
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Click on register button"):
            register_button = ios_landing.register_button
            expect(register_button).to_have(values.REGISTER, ElementAttribute.LABEL)
            register_button.click()
            expect(register_page.register_screen_title).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(register_page.register_heading_text).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(register_page.register_subtitle_text).to_have(
                values.REGISTER_CREATE_ACCOUNT_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("Click on back button to return to landing page"):
            back_button = ios_landing.back_navigation_button
            expect(back_button).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
            back_button.click()
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Click on sign in button"):
            sign_in_button = ios_landing.sign_in_button
            expect(sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            back_button = ios_landing.back_navigation_button
            expect(back_button).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
            back_button.click()
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)
