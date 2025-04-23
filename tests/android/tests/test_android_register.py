"""
Register Test Module
"""

import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_register import AndroidRegister
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals
from tests.common.utils import generate_random_credentials


@pytest.mark.ANDROID_REGRESSION
class TestAndroidRegister:
    """
    Register screen's Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify register screen is loaded successfully
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f"Starting {TestAndroidRegister.__name__} Test Case")
        android_landing = AndroidLanding()
        android_register = AndroidRegister()

        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        assert android_landing.get_register_button.exists()
        assert android_landing.load_register_screen()
        expect(android_register.get_register_title).to_have(values.REGISTER)
        assert android_register.go_back()
        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        assert android_landing.load_register_screen()
        expect(android_register.get_register_title).to_have(values.REGISTER)

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen,
            "This is what you will use to log in" label below, Full Name edit-field,
            "The name will be used on any certificates that you earn" label below,
            Public Username edit-field,
            "The name that will identify you in your courses. It cannot be changed later." label below,
            Password edit-field, "Your password must contain at least 8 characters, including 1 letter & 1 number.",
            "Country or Region of Residence" spinner,
            "The country or region where you live." label below, "Show optional fields" option below,
            "Create my account" button,
            "Continue with" label, "Facebook" button
            "Google" button, "or register with email" label, Email edit-field,
            "By creating an account you agree to the "edX Terms of Service and Honor Code" option
        Verify all contents/elements have default value
        Verify that user should be able to scroll screen to see all contents
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_register = AndroidRegister()

        expect(android_register.get_register_title).to_have(values.REGISTER)
        expect(android_register.get_register_title).to_have(values.REGISTER)
        expect(android_register.get_register_description).to_have(values.REGISTER_CREATE_ACCOUNT_MESSAGE)
        expect(android_register.get_txt_google_auth).to_have(values.GOOGLE_AUTH_TEXT, ElementAttribute.CONTENT_DESC)
        expect(android_register.get_txt_facebook_auth).to_have(values.FACEBOOK_AUTH_TEXT, ElementAttribute.CONTENT_DESC)
        expect(android_register.get_txt_microsoft_auth).to_have(
            values.MICROSOFT_AUTH_TEXT, ElementAttribute.CONTENT_DESC
        )
        expect(android_register.get_register_txt_name_label).to_have(values.REGISTER_FULL_NAME_TITLE)
        expect(android_register.get_register_tf_name).to_be_clickable()
        expect(android_register.get_register_txt_name_description).to_have(values.REGISTER_FULL_NAME_MESSAGE)
        expect(android_register.get_register_txt_username_label).to_have(values.REGISTER_PUBLIC_USERNAME_TITLE)
        expect(android_register.get_register_tf_username).to_be_clickable()
        expect(android_register.get_register_txt_username_description).to_have(values.REGISTER_PUBLIC_USERNAME_MESSAGE)
        expect(android_register.get_register_txt_email_label).to_have(values.REGISTER_EMAIL_TITLE)
        expect(android_register.get_register_tf_email).to_be_clickable()
        expect(android_register.get_register_txt_email_description).to_have(values.REGISTER_EMAIL_MESSAGE)
        expect(android_register.get_register_txt_password_label).to_have(values.REGISTER_PASSWORD_TITLE)
        expect(android_register.get_register_tf_password).to_be_clickable()
        android_register.get_register_txt_password_label.scroll_vertically_from_element()
        expect(android_register.get_register_txt_password_description).to_have(values.REGISTER_PASSWORD_MESSAGE)
        expect(android_register.get_register_txt_country_label).to_have(values.REGISTER_COUNTRY_TITLE)

        android_register.get_register_tf_password.scroll_vertically_from_element()
        expect(android_register.get_register_tf_country).to_be_clickable()
        expect(android_register.get_register_txt_country_description).to_have(values.REGISTER_COUNTRY_MESSAGE)
        expect(
            android_register.honor_policy_text,
            "privacy honor text not found on registration screen",
        ).to_be_displayed()
        assert android_register.get_register_txt_optional_field.exists()
        expect(android_register.get_register_btn_create_account).to_be_clickable()

    def test_fields_error_description_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify on clicking create button all fields should show error message,
        Following fields will show error message,
            Full Name, Username, Email, Password, Country
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_register = AndroidRegister()

        assert android_register.get_register_btn_create_account.click()
        expect(android_register.get_register_txt_name_description).to_have(values.REGISTER_ERROR_FULL_NAME)
        expect(android_register.get_register_txt_username_description).to_have(values.REGISTER_ERROR_USER_NAME)
        expect(android_register.get_register_txt_email_description).to_have(values.REGISTER_ERROR_EMAIL)
        android_register.get_register_txt_email_description.scroll_vertically_from_element()
        expect(android_register.get_register_txt_password_description).to_have(values.REGISTER_ERROR_PASSWORD)
        expect(android_register.get_register_txt_country_description).to_have(values.REGISTER_ERROR_SELECT_COUNTRY)

    def test_show_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on clicking optional fields,
            "Level of Education" label and placeholder,
            "Gender" label and placeholder
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_register = AndroidRegister()

        assert android_register.get_register_txt_optional_field.click()
        expect(android_register.get_register_education_level).to_have(values.REGISTER_EDUCATION_LEVEL)
        expect(android_register.get_register_education_level_placeholder).to_have(
            values.REGISTER_EDUCATION_LEVEL_PLACEHOLDER
        )
        expect(android_register.get_register_gender_label).to_have(values.REGISTER_GENDER_LABEL)
        expect(android_register.get_gender_label_placeholder).to_have(values.REGISTER_GENDER_LABEL)

    def test_account_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following fields are filled with valid data,
            Full Name, Username, Email, Password, Country,
        Verify user should be able to click on create account button,
        Verify main dashboard screen is loaded successfully
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_register = AndroidRegister()
        global_contents = Globals(setup_logging)
        main_dashboard_page = AndroidMainDashboard()

        user_name = generate_random_credentials(5)
        email = user_name + "@example.com"
        first_name = generate_random_credentials(4)
        last_name = generate_random_credentials(4)
        full_name = first_name + " " + last_name
        password = generate_random_credentials(6) + global_contents.login_password

        assert android_register.go_back()
        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        assert android_landing.load_register_screen()
        expect(android_register.screen_title).to_have(values.REGISTER)
        expect(android_register.get_register_title).to_have(values.REGISTER)

        assert android_register.get_register_tf_name.send_keys(full_name)
        assert android_register.get_register_tf_username.send_keys(user_name)
        assert android_register.get_register_tf_email.send_keys(email)
        assert android_register.get_register_tf_password.send_keys(password)

        android_register.get_register_tf_password.scroll_vertically_from_element()
        assert android_register.get_register_tf_country.click()
        expect(android_register.get_register_country_selection_dialogue).to_have(values.REGISTER_COUNTRY_PICKER_TITLE)
        assert android_register.country_search.send_keys("United States of America")
        assert android_register.get_txt_us_title.click()
        assert android_register.get_register_btn_create_account.click()
        expect(main_dashboard_page.learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
