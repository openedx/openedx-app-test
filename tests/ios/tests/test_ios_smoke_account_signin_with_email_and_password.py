"""
iOS - SMOKE - Signin with Email and Password
"""

import allure
import pytest

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew


@allure.epic("Accounts")
@allure.feature("Sign In")
@allure.story("user can sign in with email and password")
@allure.suite("IOS SMOKE")
@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestAccountSignInWithEmailAndPassword:
    """Test Account Sign In with Email and Password"""

    def test_account_signin_with_email_and_password(self, set_capabilities, setup_logging):
        """
        Verify sign in flow with email and password
        """
        Element.set_logger(setup_logging)
        Element.set_driver(set_capabilities)
        logger = setup_logging
        ios_landing_page = IosLanding()
        ios_login_page = IosLogin()
        whats_new_page = IosWhatsNew()
        my_courses_list = IosMyCoursesList()
        main_dashboard_page = IosMainDashboard()
        ios_profile_page = IosProfile()
        global_contents = Globals(setup_logging)

        with allure.step("Dismiss notifications pop-up if exists"):
            if ios_landing_page.allow_notifications_button.exists(raise_exception=False):
                ios_landing_page.allow_notifications_button.click()

        with allure.step("verify “Sign in“ button exists on landing page"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on Sign in button"):
            ios_landing_page.sign_in_button.click()
            expect(ios_login_page.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Enter a valid email or username"):
            ios_login_page.username_textfield.send_keys(global_contents.login_user_name + "\n")

        with allure.step("Enter a valid password"):
            ios_login_page.password_textfield.send_keys(global_contents.login_password + "\n")

        with allure.step("Click on Sign in button"):
            ios_login_page.signin_button.click()
            logger.info(f"{global_contents.login_user_name} is successfully logged in")

        with allure.step("Verify learn tab is loaded"):
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()
            expect(my_courses_list.my_courses_header_text).to_have(
                values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.LABEL
            )

        with allure.step("Goto Profile Tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            expect(ios_profile_page.full_name_label).to_have(values.PROFILE_NAME_TEXT, ElementAttribute.LABEL)
            expect(ios_profile_page.username_label).to_have(
                f"@{global_contents.login_user_name}", ElementAttribute.LABEL
            )

        with allure.step("click on settings icon"):
            ios_profile_page.profile_settings_button.click()

        with allure.step("Click on log out button"):
            Element.swipe_vertical_full_page()
            Element.swipe_vertical_full_page()
            ios_profile_page.profile_logout_button.click()
            logger.info("clicking log out")

        with allure.step("Click on Log out button on the confirmation prompt"):
            ios_profile_page.get_logout_button_from_prompt.click()
            logger.info("log out successful")

        with allure.step("verify landing page loads and sign in button is visible"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
