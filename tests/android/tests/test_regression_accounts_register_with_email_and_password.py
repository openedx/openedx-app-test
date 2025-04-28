"""
Register Test Module
"""

from time import sleep

import allure
import pytest
from framework import expect
from framework.element import Element
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_register import AndroidRegister
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.enums import ScrollDirections
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals


@allure.epic("Accounts")
@allure.feature("Registration")
@allure.story("Register with email and password")
@pytest.mark.ANDROID_REGRESSION
class TestAndroidRegister:
    """
    Register screen's Test Case
    """

    def test_register_with_email_and_password(self, set_capabilities, setup_logging):
        """
        Verify complete registration flow with email and password
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        landing_page = AndroidLanding()
        register_page = AndroidRegister()
        profile_page = AndroidProfile()
        sign_in_page = AndroidSignIn()
        main_dashboard = AndroidMainDashboard()
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()

        with allure.step("verify 'Register' button exists on landing page"):
            assert landing_page.register_button.exists()
            expect(landing_page.register_button_text).to_have(values.REGISTER)

        with allure.step("Click on Register button"):
            assert landing_page.register_button.click()
            expect(register_page.screen_title).to_have(values.REGISTER)
            expect(register_page.register_title).to_have(values.REGISTER)
            expect(register_page.register_description).to_have(values.REGISTER_CREATE_ACCOUNT_MESSAGE)

        with allure.step("Verify field headings and descriptions"):
            expect(register_page.get_txt_google_auth).to_have(values.GOOGLE_AUTH_TEXT, ElementAttribute.CONTENT_DESC)
            expect(register_page.get_txt_facebook_auth).to_have(
                values.FACEBOOK_AUTH_TEXT, ElementAttribute.CONTENT_DESC
            )
            expect(register_page.get_txt_microsoft_auth).to_have(
                values.MICROSOFT_AUTH_TEXT, ElementAttribute.CONTENT_DESC
            )
            expect(register_page.name_field_label).to_have(values.REGISTER_FULL_NAME_TITLE)
            expect(register_page.name_text_field).to_be_clickable()
            expect(register_page.name_field_description).to_have(values.REGISTER_FULL_NAME_MESSAGE)
            expect(register_page.username_field_label).to_have(values.REGISTER_PUBLIC_USERNAME_TITLE)
            expect(register_page.username_text_field).to_be_clickable()
            expect(register_page.username_field_description).to_have(values.REGISTER_PUBLIC_USERNAME_MESSAGE)
            expect(register_page.email_field_label).to_have(values.REGISTER_EMAIL_TITLE)
            expect(register_page.email_text_field).to_be_clickable()
            expect(register_page.email_field_description).to_have(values.REGISTER_EMAIL_MESSAGE)
            expect(register_page.password_field_label).to_have(values.REGISTER_PASSWORD_TITLE)
            expect(register_page.password_text_field).to_be_clickable()

            Element.swipe_vertical_full_page()

            expect(register_page.password_field_description).to_have(values.REGISTER_PASSWORD_MESSAGE)
            expect(register_page.country_field_label).to_have(values.REGISTER_COUNTRY_TITLE)
            expect(register_page.country_text_field).to_be_clickable()
            expect(register_page.country_field_description).to_have(values.REGISTER_COUNTRY_MESSAGE)

        with allure.step("Leave all fields empty and click on Create account button"):
            assert register_page.btn_create_account.click()

        with allure.step("verify empty field validations"):
            expect(register_page.name_field_description).to_have(values.REGISTER_ERROR_FULL_NAME)
            expect(register_page.username_field_description).to_have(values.REGISTER_ERROR_USER_NAME)
            expect(register_page.email_field_description).to_have(values.REGISTER_ERROR_EMAIL)
            Element.swipe_vertical_full_page()
            expect(register_page.password_field_description).to_have(values.REGISTER_ERROR_PASSWORD)
            expect(register_page.country_field_description).to_have(values.REGISTER_ERROR_SELECT_COUNTRY)

        with allure.step("Enter Full Name and verify error message changes"):
            Element.swipe_vertical_full_page(ScrollDirections.DOWN)
            full_name = global_contents.generate_random_credentials(6)
            register_page.name_text_field.send_keys(full_name)
            sleep(5)
            expect(register_page.name_field_description).to_have(values.REGISTER_FULL_NAME_MESSAGE)

        with allure.step("Verify username with blank space not valid"):
            register_page.username_text_field.send_keys("john doe")
            register_page.btn_create_account.scroll_into_view().click()
            Element.swipe_vertical_full_page(ScrollDirections.DOWN)
            expect(register_page.username_field_description).to_have(values.REGISTER_ERROR_USER_NAME_BLANK_SPACE)

        with allure.step("Enter a valid username"):
            register_page.username_text_field.clear()
            username = global_contents.generate_random_credentials(6)
            register_page.username_text_field.send_keys(username)
            expect(register_page.username_field_description).to_have(values.REGISTER_PUBLIC_USERNAME_MESSAGE)

        with allure.step("Verify email validation"):
            register_page.email_text_field.send_keys("abc@gmail")
            register_page.btn_create_account.scroll_into_view().click()
            Element.swipe_vertical_full_page(ScrollDirections.DOWN)
            expect(register_page.email_field_description).to_have(values.REGISTER_ERROR_EMAIL_INVALID)

        with allure.step("Enter an already registered email “abc@gmail.com”"):
            register_page.email_text_field.clear()
            register_page.email_text_field.send_keys("abc@gmail.com")
            register_page.btn_create_account.scroll_into_view().click()
            sleep(3)
            expect(register_page.email_field_description).to_have(
                "This email is already associated with an existing account"
            )

        with allure.step("Enter a valid unregistered email"):
            register_page.email_text_field.clear()
            email = f"{global_contents.generate_random_credentials(6)}@yopmail.com"
            register_page.email_text_field.send_keys(email)
            expect(register_page.email_field_description).to_have(values.REGISTER_EMAIL_MESSAGE)

        with allure.step("Verify password validation"):
            test_passwords = ["abpzjedfgio", "12007691", "1a2b3c", "abc12345"]
            expected_errors = [
                "This password must contain at least 1 number.",
                "This password must contain at least 1 letter.",
                "This password is too short. It must contain at least 8 characters.",
                "This password is too common.",
            ]

            for password, error in zip(test_passwords, expected_errors):
                Element.swipe_vertical_full_page()
                register_page.password_text_field.clear()
                register_page.password_text_field.send_keys(password)
                register_page.btn_create_account.click()
                sleep(3)
                expect(register_page.password_field_description).to_contain(error)

        with allure.step("Enter a valid password"):
            register_page.password_text_field.clear()
            password = global_contents.generate_random_credentials(8) + "123"
            register_page.password_text_field.send_keys(password)
            expect(register_page.password_field_description).to_have(values.REGISTER_PASSWORD_MESSAGE)

        with allure.step("Open country/region picker dropdown"):
            register_page.country_text_field.scroll_into_view().click()
            expect(register_page.get_register_country_selection_dialogue).to_have(values.REGISTER_COUNTRY_PICKER_TITLE)
        with allure.step("Search for a country and select it"):
            register_page.search_field.send_keys(values.REGISTER_COUNTRY)
            assert register_page.get_txt_us_title.click()
            expect(register_page.country_text_field).to_have(values.REGISTER_COUNTRY)

        with allure.step("Verify marketing messages agreement checkbox and toggle it"):
            register_page.marketing_messages_agreement_check_box.scroll_into_view()
            expect(register_page.marketing_messages_agreement_check_box).to_be_checked()
            assert register_page.marketing_messages_agreement_check_box.click()
            expect(register_page.marketing_messages_agreement_check_box).not_.to_be_checked()

        with allure.step("Click on show optional fields button"):
            register_page.show_optional_field.click()
            register_page.btn_create_account.scroll_into_view()
            expect(register_page.highest_level_of_education_field_label).to_have(values.REGISTER_EDUCATION_LEVEL)
            expect(register_page.gender_field_label).to_have(values.REGISTER_GENDER_LABEL)

        with allure.step("Click on education level dropdown"):
            assert register_page.education_level_dropdown.click()

        with allure.step("search for an education level and click on it"):
            register_page.search_field.send_keys("Bachelor's degree")
            assert register_page.bachelor_level_education.click()
            expect(register_page.education_level_dropdown).to_have("Bachelor's degree")

        with allure.step("click on Gender dropdown"):
            assert register_page.gender_field_dropdown.wait_for_clickable().click()
            if not register_page.search_field.exists(raise_exception=False):
                assert register_page.gender_field_dropdown.click()
            assert register_page.gender_male_option.exists()
            assert register_page.gender_other_option.exists()
            assert register_page.gender_female_option.exists()

        with allure.step("Search for a Gender option and click on it"):
            register_page.search_field.send_keys("Male")
            assert register_page.gender_male_option.click()
            expect(register_page.gender_field_dropdown).to_have("Male")

        with allure.step("Click on hide optional fields button"):
            register_page.show_optional_field.click()
            sleep(3)
            expect(register_page.gender_field_dropdown).not_.to_be_displayed()
            expect(register_page.bachelor_level_education).not_.to_be_displayed()

        with allure.step("Click on show optional fields button"):
            register_page.show_optional_field.click()
            sleep(3)
            expect(register_page.gender_field_dropdown).to_have("Male")
            expect(register_page.education_level_dropdown).to_have("Bachelor's degree")

        with allure.step("verify honor text"):
            assert register_page.find_by_text_on_screen(
                "By creating an account, you agree to the edX End User Licence Agreement and edX Terms of Service and"
                " Honor Code and you acknowledge that edX and each Member process your personal data in accordance with"
                " the edX Privacy Policy."
            )

        with allure.step("Create account and verify Learn Tab"):
            assert register_page.btn_create_account.scroll_into_view().wait_for_clickable().click()

        with allure.step("Verify Learn Tab is loaded after completion"):
            expect(main_dashboard.learn_tab).to_be_displayed()
            expect(main_dashboard.learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)

        with allure.step("Goto Profile Tab and verify username and Full name"):
            assert main_dashboard.profile_tab.click()
            expect(profile_page.profile_username).to_have(f"@{username}")
            expect(profile_page.profile_txt_name).to_have(full_name)

        with allure.step("Verify profile and perform logout"):
            assert profile_page.settings_button.click()
            assert profile_page.get_profile_txt_settings.is_displayed()

        with allure.step("Click on Log out button"):
            assert profile_page.profile_txt_logout.scroll_into_view().click()
            expect(profile_page.logout_prompt_msg).to_have("Are you sure you want to log out?")

        with allure.step("click on Log out button on the confirmation prompt"):
            expect(profile_page.logout_prompt_logout_button_text).to_have("Log Out")
            assert profile_page.logout_prompt_logout_button.click()
            assert landing_page.register_button.exists()

        with allure.step("sign in with created account"):
            assert landing_page.signin_button.exists()
            assert landing_page.load_signin_screen()
            assert sign_in_page.sign_in_tf_email.send_keys(username)
            assert sign_in_page.sign_in_password_field.send_keys(password)
            assert sign_in_page.signin_button.click()
            if global_contents.whats_new_enable:
                assert whats_new_page.get_close_button.click()

        with allure.step("Verify Learn Tab is loaded after completion"):
            expect(main_dashboard.learn_tab).to_be_displayed()
            expect(main_dashboard.learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)

        with allure.step("Goto Profile Tab and verify username and Full name"):
            assert main_dashboard.profile_tab.click()
            expect(profile_page.profile_username).to_have(f"@{username}")
            expect(profile_page.profile_txt_name).to_have(full_name)

        with allure.step("Delete account - Clean up"):
            assert profile_page.settings_button.click()
            assert profile_page.profile_settings_manage_account.click()
            assert profile_page.profile_settings_delete_account.click()
            assert profile_page.profile_settings_password_input.send_keys(password)
            assert profile_page.profile_settings_delete_account_confirm.click()
            assert landing_page.register_button.exists()
