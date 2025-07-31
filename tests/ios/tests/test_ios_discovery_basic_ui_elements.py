"""
Discovery Screen Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute

from tests.common import values
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_register import IosRegister


@pytest.mark.IOS
@pytest.mark.IOS_DISCOVERY
@pytest.mark.IOS_SMOKE
class TestIosDiscoveryBasicUiElements:
    """Discovery screen basic UI Elements"""

    def test_ios_discover_basic_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            1. App starts and landing page is loaded.
               - Verify edx logo image and explore all courses button exists.
            2. Click on explore all courses button.
               - Discover page is loaded.
               - Wait for loading circle to complete.
               - Screen title shows “Discover”.
               - Verify heading title:
             “Build skills. Earn a certificate. Advance your career.”
               - Verify edX xpert chat bot button appears with label:
             “Open XPERT Chatbot“
               - Verify xpert dialogue: “I'm Xpert, an AI assistant to help you find things.“
               - Verify close button exists on dialogue: “Close proactive message“.
            3. Click on the close button on dialogue.
               - The dialogue message disappears.
               - Verify Register button and sign in button exists.
            4. Click on Register button.
               - Verify register screen opens.
               - Verify register screen title “Register”.
            5. Click on back button.
               - Verify discovery page is loaded.
            6. Click on Sign in button.
               - Verify sign in screen is loaded.
            7. Click on back button.
               - Discover page is loaded.
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)

        ios_landing = IosLanding()
        ios_discover_page = IosDiscoverPage()
        ios_register_page = IosRegister()
        ios_login_page = IosLogin()

        with allure.step("Verify landing page is loaded successfully"):
            logo_image = ios_landing.edx_logo_image
            expect(logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.explore_all_courses_button).to_have(
                values.LANDING_EXPLORE_COURSES, ElementAttribute.LABEL
            )

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Verify discover screen is loaded successfully"):
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)

        with allure.step("Verify heading title is displayed"):
            expect(ios_discover_page.heading_title_part1).to_have(
                values.DISCOVER_SCREEN_HEADING_PART1, ElementAttribute.LABEL
            )
            expect(ios_discover_page.heading_title_part2).to_have(
                values.DISCOVER_SCREEN_HEADING_PART2, ElementAttribute.LABEL
            )

        with allure.step("Verify edx chat bot button is displayed"):
            expect(ios_discover_page.openedx_ai_chat_bot).to_exist()
            expect(ios_discover_page.openedx_ai_chat_bot).to_have(
                values.OPEN_XPERT_CHATBOT_LABEL, ElementAttribute.LABEL
            )
            if ios_discover_page.openedx_ai_chat_bot_web_alert.exists(raise_exception=False):
                ios_discover_page.openedx_ai_chat_bot_web_alert.get_child_element(
                    ios_discover_page.openedx_ai_chat_bot_dialogue_msg
                )

        with allure.step("Click on the close button on dialogue"):
            ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.ai_assistant_dismiss_button).not_.to_exist()
            expect(ios_discover_page.openedx_ai_chat_bot).to_exist()

        with allure.step("Verify Register button and sign in button exists"):
            expect(ios_landing.register_button).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(ios_landing.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on Register button"):
            ios_landing.register_button.click()
            expect(ios_register_page.register_screen_title).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(ios_register_page.register_heading_text).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(ios_register_page.register_subtitle_text).to_have(
                values.REGISTER_CREATE_ACCOUNT_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("Click on back button"):
            ios_register_page.back_navigation_button.click()
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )

        with allure.step("Click on Sign In button"):
            ios_landing.sign_in_button.click()
            expect(ios_login_page.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            expect(ios_login_page.signin_welcome_text).to_have(values.SIGN_IN_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Click on back button"):
            ios_register_page.back_navigation_button.click()
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
