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
@allure.story("user can only sign in with valid email and password")
@allure.suite("IOS REGRESSION")
@pytest.mark.IOS
@pytest.mark.IOS_REGRESSION
class TestAccountSignInWithEmailAndPassword:
    """Test Account Sign In with Email and Password"""

    def test_account_signin_with_email_and_password(self, set_capabilities, setup_logging):
        """
        Verify sign in flow with email and password

        Steps:
        1. Launch app and verify “Sign in“ button exists on landing page.
        2. Click on Sign in button. Verify Sign in screen is loaded with title “Sign in” and description
           ”Welcome back! Sign in to access your courses.” Verify field headings: Email or Username, Password.
        3. Leave all fields empty and click on Sign In button. Verify error messages for required fields.
        4. Enter invalid username (e.g., “john doe”) and correct password, click Sign in.
                Verify invalid credentials toast.
        5. Enter valid, unregistered username and correct password, click Sign in. Verify invalid credentials toast.
        6. Enter invalid email (e.g., “abc@gmail”) and click Sign in. Verify invalid credentials toast.
        7. Enter valid but unregistered email (e.g., “abc@gmail.com”) and click Sign in.
                Verify invalid credentials toast.
        8. Clear out the Email or username field and click Sign in. Verify error for missing username/email.
        9. Enter valid username, clear password field, click Sign in. Verify error for missing password.
        10. Enter invalid password and click Sign in. Verify invalid credentials toast.
        11. Verify eye icon on password field is clickable. Enter valid password and sign in. Verify Learn tab loads.
        12. Go to Profile Tab. Verify username and full name.
        13. Click Settings icon. Verify Settings screen title.
        14. Scroll to log out button. Verify text is “Log Out”.
        15. Click Log out button. Verify prompt “Are you sure you want to log out?” appears.
        16. Click Log out on confirmation prompt. Verify landing page loads.
        17. Click Sign in button.
        18. Enter valid email and password.
        19. Click Sign in button. Verify Learn tab loads.
        20. Go to Profile Tab. Verify username and full name.
        21. Click settings button. Verify Settings screen title is “Settings”.
        22. Scroll and click Log out button. Verify prompt “Are you sure you want to log out?” and close button exist.
        23. Click close button. Verify prompt disappears.
        24. Click Log out button. Verify Log out button exists on prompt with text “Log Out”.
        25. Verify landing page loads and sign in button is visible.
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

        # test data
        invalid_email = "invalid_email@yop"
        invalid_username = "invalid username"
        valid_unregistered_username = "john_doe"
        valid_unregistered_email = "john_doe@yopmail.com"
        invalid_password = "invalidpassword"

        with allure.step("Dismiss notifications pop-up if exists"):
            if ios_landing_page.allow_notifications_button.exists(raise_exception=False):
                ios_landing_page.allow_notifications_button.click()

        with allure.step("verify “Sign in“ button exists on landing page"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on Sign in button"):
            ios_landing_page.sign_in_button.click()
            expect(ios_login_page.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            expect(ios_login_page.signin_welcome_text).to_have(values.SIGN_IN_MESSAGE, ElementAttribute.LABEL)

        with allure.step("verify username and password field headings texts"):
            expect(ios_login_page.username_text_field_label).to_have(
                values.EMAIL_OR_USERNAME_IOS, ElementAttribute.LABEL
            )
            expect(ios_login_page.username_text_field_placeholder).to_have(
                values.EMAIL_OR_USERNAME_IOS, ElementAttribute.LABEL
            )
            expect(ios_login_page.password_text_field_label).to_have(values.PASSWORD, ElementAttribute.LABEL)
            expect(ios_login_page.password_textfield_placeholder).to_have(values.PASSWORD, ElementAttribute.LABEL)

        with allure.step("Leave all fields empty and click on Sign In button"):
            Element.swipe_vertical_full_page()
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_EMAIL_ADDRESS_OR_PASSWORD, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=20)

        with allure.step("Enter invalid username & click signin"):
            ios_login_page.username_textfield.send_keys(invalid_username + "\n")
            ios_login_page.password_textfield.send_keys(global_contents.login_password + "\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Enter invalid email & click signin"):
            ios_login_page.username_textfield.clear_and_type(invalid_email + "\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_EMAIL_ADDRESS_OR_PASSWORD, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Enter a valid unregistered username"):
            ios_login_page.username_textfield.clear_and_type(valid_unregistered_username + "\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Enter a valid unregistered email or username"):
            ios_login_page.username_textfield.clear_and_type(valid_unregistered_email + "\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Clear out the Email or username field and click on Sign in button"):
            ios_login_page.username_textfield.clear_and_type("\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_EMAIL_ADDRESS_OR_PASSWORD, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Enter a valid username and clear out the password field and hit Sign in button"):
            ios_login_page.username_textfield.send_keys(global_contents.login_user_name + "\n")
            ios_login_page.password_textfield.clear_and_type("\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(values.INVALID_PASSWORD_LENGTH, ElementAttribute.LABEL)
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=30)

        with allure.step("Enter an invalid password and hit sign in button"):
            ios_login_page.password_textfield.send_keys(invalid_password + "\n")
            ios_login_page.signin_button.click()
            expect(ios_login_page.snackbar_text_message).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
            ios_login_page.snackbar_text_message.wait_to_disappear(timeout=20)

        with allure.step("verify password field eye toggle"):
            expect(ios_login_page.password_field_eye_button).to_have(values.HIDE_PASSWORD, ElementAttribute.LABEL)
            ios_login_page.password_field_eye_button.click()
            expect(ios_login_page.password_field_eye_button).to_have(values.SHOW_PASSWORD, ElementAttribute.LABEL)
            ios_login_page.password_field_eye_button.click()
            expect(ios_login_page.password_field_eye_button).to_have(values.HIDE_PASSWORD, ElementAttribute.LABEL)

        with allure.step("Enter a valid password"):
            ios_login_page.password_textfield.clear_and_type(global_contents.login_password + "\n")

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
            expect(ios_profile_page.settings_screen_title).to_have(
                values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL
            )

        with allure.step("Click on log out button"):
            Element.swipe_vertical_full_page()
            Element.swipe_vertical_full_page()
            expect(ios_profile_page.profile_logout_button).to_have(values.LOG_OUT_TEXT, ElementAttribute.LABEL)
            ios_profile_page.profile_logout_button.click()
            logger.info("clicking log out")

        with allure.step("Click on Log out button on the confirmation prompt"):
            expect(ios_profile_page.find_by_text_on_screen(values.LOGOUT_DIALOG_TITLE)).to_exist()
            ios_profile_page.get_logout_button_from_prompt.click()
            logger.info("log out successful")

        with allure.step("verify landing page loads and sign in button is visible"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on Sign in button"):
            ios_landing_page.sign_in_button.click()
            expect(ios_login_page.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Enter a valid email and password and hit Sign in button"):
            ios_login_page.username_textfield.send_keys(values.AUTOMATION_USER_EMAIL + "\n")
            ios_login_page.password_textfield.send_keys(global_contents.login_password + "\n")
            ios_login_page.signin_button.click()

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
            expect(ios_profile_page.settings_screen_title).to_have(
                values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL
            )

        with allure.step("Click on log out button"):
            Element.swipe_vertical_full_page()
            Element.swipe_vertical_full_page()
            expect(ios_profile_page.profile_logout_button).to_have(values.LOG_OUT_TEXT, ElementAttribute.LABEL)
            ios_profile_page.profile_logout_button.click()
            logger.info("clicking log out")

        with allure.step("Click on Log out button on the confirmation prompt"):
            expect(ios_profile_page.find_by_text_on_screen(values.LOGOUT_DIALOG_TITLE)).to_exist()
            ios_profile_page.get_logout_button_from_prompt.click()
            logger.info("log out successful")

        with allure.step("verify landing page loads and sign in button is visible"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
