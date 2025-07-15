"""iOS - Regression - Account Registration - Sign Up with Email and Password Test Module"""

import pytest
import allure

from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute, ScrollDirections, GenderOptions
from tests.common.enums.general_enums import EducationLevel
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_register import IosRegister
from tests.ios.pages.ios_whats_new import IosWhatsNew


@allure.epic("Accounts")
@allure.feature("Account Registration")
@allure.story("Sign Up with Email and Password")
@pytest.mark.IOS_REGRESSION
class TestAccountRegistrationSignupWithEmailAndPassword:
    """Regression test for account registration using email and password on iOS."""

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

        user_name = "TestAuto_" + global_contents.generate_random_credentials(5)
        invalid_email = "john.doe@"
        registered_email = "abc@gmail.com"
        email = user_name + "@yopmail.com"
        invalid_username = "john doe"
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
            expect(register_page.get_signup_text).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(register_page.get_signup_subtitle_text).to_have(
                values.REGISTER_CREATE_ACCOUNT_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("verify social login buttons exist"):
            expect(register_page.get_social_auth_title_text).to_have(
                values.REGISTER_OPTIONS_TITLE, ElementAttribute.LABEL
            )
            expect(register_page.social_auth_google_button).to_have(values.GOOGLE_SIGNIN, ElementAttribute.LABEL)
            expect(register_page.social_auth_facebook_button).to_have(values.FACEBOOK_SIGNIN, ElementAttribute.LABEL)
            expect(register_page.social_auth_microsoft_button).to_have(values.MICROSOFT_SIGNIN, ElementAttribute.LABEL)
            expect(register_page.social_auth_apple_button).to_have(values.APPLE_SIGNIN, ElementAttribute.LABEL)

        with allure.step("verify field heading and instruction text/hind"):
            # Full name field
            expect(register_page.name_text_field_label).to_have(values.REGISTER_FULL_NAME_TITLE, ElementAttribute.LABEL)
            expect(register_page.name_text_field).to_be_visible()
            expect(register_page.name_instructions_text).to_have(
                values.REGISTER_FULL_NAME_MESSAGE, ElementAttribute.LABEL
            )
            # Username field
            expect(register_page.username_text_field_label).to_have(
                values.REGISTER_PUBLIC_USERNAME_TITLE, ElementAttribute.LABEL
            )
            expect(register_page.username_text_field).to_be_visible()
            expect(register_page.username_instructions_text).to_have(
                values.REGISTER_PUBLIC_USERNAME_MESSAGE, ElementAttribute.LABEL
            )
            # Email field
            expect(register_page.email_text_field_label).to_have(values.REGISTER_EMAIL_TITLE, ElementAttribute.LABEL)
            expect(register_page.email_text_field).to_be_visible()
            expect(register_page.email_instructions_text).to_have(values.REGISTER_EMAIL_MESSAGE, ElementAttribute.LABEL)
            register_page.create_account_button.scroll_and_find()
            # Password field
            expect(register_page.password_text_field_label).to_have(
                values.REGISTER_PASSWORD_TITLE, ElementAttribute.LABEL
            )
            expect(register_page.password_text_field).to_be_visible()
            expect(register_page.password_instructions_text).to_have(
                values.REGISTER_PASSWORD_MESSAGE, ElementAttribute.LABEL
            )
            # Country Picker
            expect(register_page.country_text_field_label).to_have(
                values.REGISTER_COUNTRY_TITLE, ElementAttribute.LABEL
            )
            expect(register_page.country_picker_button).to_exist()
            expect(register_page.country_instructions_text).to_have(
                values.REGISTER_COUNTRY_MESSAGE, ElementAttribute.LABEL
            )
            # Optional fields
            expect(register_page.optional_fields_toggle_buttons).to_have(
                values.REGISTER_SHOW_OPTIONAL_FIELDS, ElementAttribute.LABEL
            )
            expect(register_page.create_account_button).to_have(
                values.CREATE_ACCOUNT_BUTTON_LABEL, ElementAttribute.LABEL
            )

        with allure.step("leave all fields empty and click on create account button"):
            register_page.create_account_button.click()

        with allure.step("error messages verification"):
            expect(register_page.name_instructions_text).to_have(
                values.REGISTER_ERROR_FULL_NAME, ElementAttribute.LABEL
            )
            expect(register_page.username_instructions_text).to_have(
                values.REGISTER_ERROR_USER_NAME, ElementAttribute.LABEL
            )
            expect(register_page.email_instructions_text).to_have(values.REGISTER_ERROR_EMAIL, ElementAttribute.LABEL)
            Element.swipe_vertical_full_page()
            expect(register_page.password_instructions_text).to_have(
                values.REGISTER_ERROR_PASSWORD, ElementAttribute.LABEL
            )
            expect(register_page.country_instructions_text).to_have(
                values.REGISTER_ERROR_SELECT_COUNTRY, ElementAttribute.LABEL
            )
            Element.swipe_vertical_full_page(ScrollDirections.DOWN)

        with allure.step("Enter Full Name"):
            register_page.name_text_field.send_keys(full_name + "\n")
            register_page.create_account_button.scroll_and_find().click()
            expect(register_page.name_instructions_text).to_have(
                values.REGISTER_FULL_NAME_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("Enter a invalid username"):
            register_page.username_text_field.click()
            register_page.username_text_field.send_keys(invalid_username + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify invalid username error message"):
            expect(register_page.username_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_ERROR_USER_NAME_BLANK_SPACE)
            expect(register_page.username_instructions_text).to_have(
                values.REGISTER_ERROR_USER_NAME_BLANK_SPACE, ElementAttribute.LABEL
            )

        with allure.step("Enter a valid username"):
            register_page.username_text_field.clear_and_type(user_name + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify invalid username error message disappear"):
            expect(register_page.username_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_PUBLIC_USERNAME_MESSAGE)
            expect(register_page.username_instructions_text).to_have(
                values.REGISTER_PUBLIC_USERNAME_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("Enter a invalid email"):
            register_page.email_text_field.click()
            register_page.email_text_field.send_keys(invalid_email + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify invalid email error message"):
            expect(register_page.email_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_ERROR_EMAIL_INVALID)
            expect(register_page.email_instructions_text).to_have(
                values.REGISTER_ERROR_EMAIL_INVALID, ElementAttribute.LABEL
            )

        with allure.step("Enter a valid registered email"):
            register_page.email_text_field.clear_and_type(registered_email + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify already registered email error message"):
            expect(register_page.email_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_EMAIL_ALREADY_EXISTS)
            expect(register_page.email_instructions_text).to_have(
                values.REGISTER_EMAIL_ALREADY_EXISTS, ElementAttribute.LABEL
            )

        with allure.step("Enter a valid unregistered email"):
            register_page.email_text_field.clear_and_type(email + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify invalid email error message disappear"):
            expect(register_page.email_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_EMAIL_MESSAGE)
            expect(register_page.email_instructions_text).to_have(values.REGISTER_EMAIL_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Test password with no numbers"):
            register_page.password_text_field.clear_and_type("abcdefgh" + "\n")
            register_page.create_account_button.scroll_and_find().click()
            expect(register_page.password_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen("This password must contain at least 1 number.", partial=True)
            expect(register_page.password_instructions_text).to_contain("This password must contain at least 1 number.")

        with allure.step("Test password with no letters"):
            register_page.password_text_field.clear_and_type("12345678" + "\n")
            register_page.create_account_button.scroll_and_find().click()
            expect(register_page.password_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen("This password must contain at least 1 letter.", partial=True)
            expect(register_page.password_instructions_text).to_contain("This password must contain at least 1 letter.")

        with allure.step("Test password that's too short"):
            register_page.password_text_field.clear_and_type("abc1234" + "\n")
            register_page.create_account_button.scroll_and_find().click()
            expect(register_page.password_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(
                "This password is too short. It must contain at least 8 characters.", partial=True
            )
            expect(register_page.password_instructions_text).to_contain(
                "This password is too short. It must contain at least 8 characters."
            )

        with allure.step("Test common password"):
            register_page.password_text_field.click()
            register_page.password_text_field.clear_and_type("abc12345" + "\n")
            register_page.create_account_button.scroll_and_find().click()
            expect(register_page.password_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen("This password is too common.", partial=True)
            expect(register_page.password_instructions_text).to_contain("This password is too common.")

        with allure.step("Enter a valid password"):
            register_page.password_text_field.click()
            register_page.password_text_field.clear_and_type(password + "\n")

        with allure.step("click on create account button"):
            register_page.create_account_button.scroll_and_find().click()

        with allure.step("verify invalid password error message disappear"):
            expect(register_page.password_instructions_text).to_be_visible()
            register_page.find_by_text_on_screen(values.REGISTER_PASSWORD_MESSAGE)
            expect(register_page.password_instructions_text).to_have(
                values.REGISTER_PASSWORD_MESSAGE, ElementAttribute.LABEL
            )

        with allure.step("Open country/region picker drop down"):
            register_page.country_picker_button.click()
            picker_title_text = register_page.picker_title_text
            expect(picker_title_text).to_have(values.REGISTER_COUNTRY_PICKER_TITLE, ElementAttribute.LABEL)

        with allure.step("Search for a country and click on it"):
            country_field = register_page.option_picker_search_field
            assert country_field.click()
            assert country_field.send_keys(values.REGISTER_COUNTRY)
            accept_button = register_page.get_picker_accept_button
            expect(accept_button).to_have(values.REGISTER_COUNTRY_ACCEPT_BUTTON, ElementAttribute.LABEL)
            assert accept_button.click()
            expect(register_page.country_picker_button).to_have(values.REGISTER_COUNTRY, ElementAttribute.LABEL)

        with allure.step("verify marketing messages agreement checkbox is checked by default"):
            expect(register_page.marketing_checkbox_selected).to_have(
                values.MARKETING_CHECKBOX_SELECTED, ElementAttribute.LABEL
            )

        with allure.step("Click the marketing agreement checkbox"):
            register_page.marketing_checkbox_selected.click()
            expect(register_page.marketing_checkbox_unselected).to_have(
                values.MARKETING_CHECKBOX_UNSELECTED, ElementAttribute.LABEL
            )

        with allure.step("click on show optional fields"):
            register_page.optional_fields_toggle_buttons.click()

        with allure.step("verify optional fields are displayed"):
            expect(register_page.highest_level_of_education_label).to_have(
                values.REGISTER_SHOW_OPTIONAL_FIELDS, ElementAttribute.LABEL
            )
            expect(register_page.gender_field_label).to_have(
                values.REGISTER_SHOW_OPTIONAL_FIELDS, ElementAttribute.LABEL
            )

        with allure.step("Select highest level of education"):
            register_page.highest_level_of_education_picker_button.click()
            expect(register_page.picker_title_text).to_have(values.REGISTER_EDUCATION_LEVEL, ElementAttribute.LABEL)
            for level in EducationLevel:
                register_page.search_and_verify_education_level_exists(level)

        with allure.step("search for an education level and click on it"):
            register_page.option_picker_search_field.clear_and_type(values.BACHELOR_DEGREE)
            register_page.get_picker_accept_button.click()

        with allure.step("verify the desired education level is selected"):
            highest_level_of_education_selected = (
                register_page.highest_level_of_education_picker_button.get_child_element(register_page.static_text)
            )
            expect(highest_level_of_education_selected).to_have(values.BACHELOR_DEGREE, ElementAttribute.LABEL)

        with allure.step("Select gender"):
            register_page.gender_picker_button.scroll_and_find().click()
            expect(register_page.picker_title_text).to_have(values.REGISTER_GENDER_LABEL, ElementAttribute.LABEL)
            for gender in GenderOptions:
                register_page.search_and_verify_gender_option_exists(gender)

        with allure.step("Search for a Gender option and click on it"):
            register_page.option_picker_search_field.clear_and_type(values.GENDER_MALE)
            register_page.get_picker_accept_button.click()
            gender_selected = register_page.gender_picker_button.get_child_element(register_page.static_text)
            expect(gender_selected).to_have(values.GENDER_MALE, ElementAttribute.LABEL)

        with allure.step("click on Hide optional fields"):
            register_page.optional_fields_toggle_buttons.click()
            optional_fields_toggle_button_label = register_page.optional_fields_toggle_buttons.get_child_element(
                register_page.static_text
            )
            expect(optional_fields_toggle_button_label).to_have(values.SHOW_OPTIONAL_FIELDS, ElementAttribute.LABEL)

        with allure.step("click on Show optional fields"):
            register_page.optional_fields_toggle_buttons.click()
            optional_fields_toggle_button_label = register_page.optional_fields_toggle_buttons.get_child_element(
                register_page.static_text
            )
            expect(optional_fields_toggle_button_label).to_have(values.HIDE_OPTIONAL_FIELDS, ElementAttribute.LABEL)

            gender_selected = register_page.gender_picker_button.get_child_element(register_page.static_text)
            expect(gender_selected).to_have(values.GENDER_MALE, ElementAttribute.LABEL)
            highest_level_of_education_selected = (
                register_page.highest_level_of_education_picker_button.get_child_element(register_page.static_text)
            )
            expect(highest_level_of_education_selected).to_have(values.BACHELOR_DEGREE, ElementAttribute.LABEL)

        with allure.step("Click on Create account button"):
            register_page.create_account_button.scroll_and_find().click()
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()
            main_dashboard_page.profile_tab.click()
            expect(ios_profile.full_name_label).to_have(full_name, ElementAttribute.LABEL)
            expect(ios_profile.username_label).to_have(f"@{user_name}", ElementAttribute.LABEL)

        with allure.step("Goto settings and logout"):
            ios_profile.profile_settings_button.click()
            ios_profile.profile_logout_button.scroll_and_find().click()
            setup_logging.info("clicking log out")
            ios_profile.get_logout_button_from_prompt.click()
            setup_logging.info("log out successful")
            expect(ios_landing_page.welcome_message, timeout=20).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)

        with allure.step("login with newly registered account"):
            ios_landing_page.sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            ios_login.username_textfield.click()
            ios_login.username_textfield.send_keys(user_name + "\n")
            ios_login.password_textfield.click()
            ios_login.password_textfield.send_keys(password + "\n")
            ios_login.signin_button.click()
            main_dashboard_page.profile_tab.exists(timeout=20)
            main_dashboard_page.profile_tab.click()
            expect(ios_profile.full_name_label).to_have(full_name, ElementAttribute.LABEL)
            expect(ios_profile.username_label).to_have(f"@{user_name}", ElementAttribute.LABEL)

        with allure.step("delete account"):
            ios_profile.profile_settings_button.click()
            ios_profile.profile_manage_account_label.click()
            ios_profile.delete_account_button.click()
            ios_profile.delete_account_password_textfield.click()
            ios_profile.delete_account_password_textfield.send_keys(password + "\n")
            ios_profile.delete_account_button.click()
            expect(ios_login.sign_in_title, timeout=20).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Try sign in with deleted account"):
            ios_login.username_textfield.click()
            ios_login.username_textfield.send_keys(user_name + "\n")
            ios_login.password_textfield.click()
            ios_login.password_textfield.send_keys(password + "\n")
            ios_login.signin_button.click()
            expect(ios_login.invalid_credentials_message, timeout=20).to_have(
                values.INVALID_CREDENTIALS_GIVEN, ElementAttribute.LABEL
            )
