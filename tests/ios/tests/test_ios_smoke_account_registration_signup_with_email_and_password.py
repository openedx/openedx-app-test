"""iOS - SMOKE - Account Registration - Sign Up with Email and Password Test Module"""

import pytest
import allure

from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_register import IosRegister
from tests.ios.pages.ios_whats_new import IosWhatsNew


@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestAccountRegistrationSignupWithEmailAndPassword:
    """Smoke test for account registration using email and password on iOS."""

    def test_account_registration_signup_with_email_and_password(self, set_capabilities, setup_logging):
        """"""
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)

        register_page = IosRegister()
        ios_landing_page = IosLanding()
        whats_new_page = IosWhatsNew()
        main_dashboard_page = IosMainDashboard()
        ios_profile = IosProfile()
        ios_login = IosLogin()
        global_contents = Globals(setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + "@yopmail.com"
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + " " + last_name
        password = "qwERt12#$5" + global_contents.generate_random_credentials(8)

        if ios_landing_page.allow_notifications_button.exists(raise_exception=False):
            ios_landing_page.allow_notifications_button.click()

        with allure.step("verify 'Register' button exists on landing page"):
            expect(ios_landing_page.register_button).to_have(values.REGISTER, ElementAttribute.LABEL)

        with allure.step("Click on Register button"):
            ios_landing_page.register_button.click()
            expect(register_page.register_screen_title).to_have(values.REGISTER, ElementAttribute.LABEL)

        with allure.step("Enter Full Name"):
            register_page.get_name_textfield.send_keys(full_name)

        with allure.step("Enter a valid username"):
            register_page.get_username_textfield.click()
            register_page.get_username_textfield.send_keys(user_name + "\n")

        with allure.step("Enter a valid unregistered email"):
            register_page.get_email_textfield.click()
            register_page.get_email_textfield.send_keys(email + "\n")
            register_page.get_password_textfield.exists()
            Element.swipe_vertical_full_page()

        with allure.step("Enter a valid password"):
            register_page.get_password_textfield.exists()
            register_page.get_password_textfield.click()
            register_page.get_password_textfield.send_keys(password + "\n")

        with allure.step("Open country/region picker drop down"):
            register_page.get_country_textfield.click()
            picker_title_text = register_page.get_picker_title_text
            expect(picker_title_text).to_have(values.REGISTER_COUNTRY_PICKER_TITLE, ElementAttribute.LABEL)

        with allure.step("Search for a country and click on it"):
            country_field = register_page.select_country
            assert country_field.click()
            assert country_field.send_keys(values.REGISTER_COUNTRY)
            accept_button = register_page.get_picker_accept_button
            expect(accept_button).to_have(values.REGISTER_COUNTRY_ACCEPT_BUTTON, ElementAttribute.LABEL)
            assert accept_button.click()
            expect(register_page.get_country_textfield).to_have(values.REGISTER_COUNTRY, ElementAttribute.LABEL)

        with allure.step("verify marketing messages agreement checkbox is checked by default"):
            expect(register_page.marketing_checkbox_selected).to_have(
                values.MARKETING_CHECKBOX_SELECTED, ElementAttribute.LABEL
            )

        with allure.step("Click the marketing agreement checkbox"):
            register_page.marketing_checkbox_selected.click()
            expect(register_page.marketing_checkbox_unselected).to_have(
                values.MARKETING_CHECKBOX_UNSELECTED, ElementAttribute.LABEL
            )

        with allure.step("Click on Create account button"):
            register_page.create_account_button.click()
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()
            main_dashboard_page.profile_tab.click()
            expect(ios_profile.profile_user_name_text).to_have(full_name, ElementAttribute.LABEL)
            expect(ios_profile.profile_user_username_text).to_have(f"@{user_name}", ElementAttribute.LABEL)

        with allure.step("Goto settings and logout"):
            ios_profile.profile_settings_button.click()
            Element.swipe_vertical_full_page()
            ios_profile.get_profile_logout_button.click()
            setup_logging.info("clicking log out")
            ios_profile.get_logout_button_from_prompt.click()
            setup_logging.info("log out successful")
            expect(ios_landing_page.get_welcome_message, timeout=20).to_have(
                values.LANDING_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("login with newly registered account"):
            ios_landing_page.sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.LOGIN, ElementAttribute.LABEL)
            ios_login.signin_username_textfield.click()
            ios_login.signin_username_textfield.send_keys(user_name + "\n")
            ios_login.signin_password_textfield.click()
            ios_login.signin_password_textfield.send_keys(password + "\n")
            ios_login.signin_button.click()
            main_dashboard_page.profile_tab.exists(timeout=20)
            main_dashboard_page.profile_tab.click()
            expect(ios_profile.profile_user_name_text).to_have(full_name, ElementAttribute.LABEL)
            expect(ios_profile.profile_user_username_text).to_have(f"@{user_name}", ElementAttribute.LABEL)

        with allure.step("delete account"):
            ios_profile.profile_settings_button.click()
            ios_profile.get_profile_manage_account_label.click()
            ios_profile.delete_account_button.click()
            ios_profile.delete_account_password_textfield.click()
            ios_profile.delete_account_password_textfield.send_keys(password + "\n")
            ios_profile.delete_account_button.click()
            expect(ios_login.sign_in_title, timeout=20).to_have(values.LOGIN, ElementAttribute.LABEL)

        with allure.step("Try sign in with deleted account"):
            ios_login.signin_username_textfield.click()
            ios_login.signin_username_textfield.send_keys(user_name + "\n")
            ios_login.signin_password_textfield.click()
            ios_login.signin_password_textfield.send_keys(password + "\n")
            ios_login.signin_button.click()
            expect(ios_login.invalid_credentials_message, timeout=20).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
