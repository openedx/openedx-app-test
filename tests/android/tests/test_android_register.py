"""
    Register Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_register import AndroidRegister
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.globals import Globals


class TestAndroidRegister:
    """
    Register screen's Test Case
    """

    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify register screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidRegister.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_register = AndroidRegister(set_capabilities, setup_logging)

        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_register_button()
        assert android_landing.load_register_screen().text == values.REGISTER
        android_register.get_back_button().click()
        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.load_register_screen().text == values.REGISTER

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen,
            "This is what you will use to login" label below, Full Name edit-field,
            "The name will be used on any certificates that you earn" label below,
            Public User Name edit-field,
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

        android_register = AndroidRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)

        assert android_register.get_register_title().text == values.REGISTER
        assert android_register.get_register_description().text == values.REGISTER_CREATE_ACCOUNT_MESSAGE
        assert android_register.get_register_txt_name_label().text == values.REGISTER_FULL_NAME_TITLE
        assert android_register.get_register_tf_name().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_register_txt_name_description().text == values.REGISTER_FULL_NAME_MESSAGE
        assert android_register.get_register_txt_username_label().text == values.REGISTER_PUBLIC_USERNAME_TITLE
        assert android_register.get_register_tf_username().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_register_txt_username_description().text == values.REGISTER_PUBLIC_USERNAME_MESSAGE
        assert android_register.get_register_txt_email_label().text == values.REGISTER_EMAIL_TITLE
        assert android_register.get_register_tf_email().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_register_txt_email_description().text == values.REGISTER_EMAIL_MESSAGE
        assert android_register.get_register_txt_password_label().text == values.REGISTER_PASSWORD_TITLE
        assert android_register.get_register_tf_password().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_register_txt_password_description().text == values.REGISTER_PASSWORD_MESSAGE
        assert android_register.get_register_txt_country_label().text == values.REGISTER_COUNTRY_TITLE

        global_contents.scroll_from_element(set_capabilities, android_register.get_register_tf_password())
        assert android_register.get_register_tf_country().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_register_txt_country_description().text == values.REGISTER_COUNTRY_MESSAGE
        privacy_honor_text = android_sign_in.get_all_textviews()[8]
        assert privacy_honor_text.text == values.REGISTER_HONOR_POLICY_TEXT
        assert android_register.get_register_txt_optional_field()
        assert android_register.get_register_btn_create_account().get_attribute('clickable') == values.TRUE_LOWERCASE
        assert android_register.get_txt_google_auth().text == values.GOOGLE_AUTH_TEXT
        assert android_register.get_txt_facebook_auth().text == values.FACEBOOK_AUTH_TEXT
        assert android_register.get_txt_microsoft_auth().text == values.MICROSOFT_AUTH_TEXT

    def test_fields_error_description_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify on clicking create button all fields should show error message,
        Following fields will show error message,
            Full Name, User Name, Email, Password, Country
        """

        android_register = AndroidRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        android_register.get_register_btn_create_account().click()
        assert android_register.get_register_txt_name_description().text == values.REGISTER_ERROR_FULL_NAME
        assert android_register.get_register_txt_username_description().text == values.REGISTER_ERROR_USER_NAME
        assert android_register.get_register_txt_email_description().text == values.REGISTER_ERROR_EMAIL
        assert android_register.get_register_txt_password_description().text == values.REGISTER_ERROR_PASSWORD
        global_contents.scroll_from_element(set_capabilities, android_register.get_register_tf_password())
        assert android_register.get_register_txt_country_description().text == values.REGISTER_ERROR_SELECT_COUNTRY

    def test_show_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on clicking optional fields,
            "Level of Education" label and placeholder,
            "Gender" label and placeholder
        """

        android_register = AndroidRegister(set_capabilities, setup_logging)

        android_register.get_register_txt_optional_field().click()
        assert android_register.get_register_education_level().text == values.REGISTER_EDUCATION_LEVEL
        assert android_register.get_register_education_level_placeholder().text == values.REGISTER_EDUCATION_LEVEL_PLACEHOLDER
        assert android_register.get_register_gender_label().text == values.REGISTER_GENDER_LABEL
        assert android_register.get_gender_label_placeholder().text == values.REGISTER_GENDER_LABEL

    def test_account_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following fields are filled with valid data,
            Full Name, User Name, Email, Password, Country,
        Verify user should be able to click on create account button,
        Verify main dashboard screen is loaded sucessfully
        """

        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_register = AndroidRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + ' ' + last_name
        password = (global_contents.generate_random_credentials(6) + global_contents.login_password)

        android_register.get_back_button().click()
        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.load_register_screen().text == values.REGISTER

        assert android_register.get_register_tf_name().send_keys(full_name)
        assert android_register.get_register_tf_username().send_keys(user_name)
        assert android_register.get_register_tf_email().send_keys(email)
        assert android_register.get_register_tf_password().send_keys(password)

        global_contents.scroll_from_element(set_capabilities, android_register.get_register_tf_password())
        android_register.get_register_tf_country().click()
        android_register.get_register_country_selection_dialogue().text == values.REGISTER_COUNTRY_PICKER_TITLE
        android_register.get_register_country_search().send_keys('United States of America')
        android_register.get_txt_US_title().click()
        android_register.get_register_btn_create_account().click()
        assert main_dashboard_page.get_learn_tab().get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
