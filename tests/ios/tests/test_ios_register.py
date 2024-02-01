"""
    Register Screen Test Module
"""

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_register import IosRegister
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin


class TestIosRegister:
    """
    Register screen's Test Case
    """

    def test_load_register_screen(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('Starting Test Case')
        register_page = IosRegister(set_capabilities, setup_logging)

        register_button = register_page.get_register_button()
        assert register_page.get_register_button().text == values.REGISTER
        register_button.click()

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen, 
                "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
                Password edit-field, "Forgot your password?" option, "Sign In" button,
                "Or sing in with" label, "Facebook" button, "Google" button
            Verify all screen contents have their default values
            Verify all fields are editable
        """

        register_page = IosRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        ios_login = IosLogin(set_capabilities, setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + ' ' + last_name
        password = (global_contents.generate_random_credentials(6) + global_contents.login_password)

        assert register_page.get_register_screen_heading().text == values.REGISTER

        back_button = ios_landing.get_back_button()
        assert back_button.text == values.LANDING_BACK_BUTTON
        sign_up_heading = register_page.get_signup_text()
        assert sign_up_heading.text == values.REGISTER_SIGN_UP_HEADING

        create_account_message = register_page.get_signup_subtitle_text()
        assert create_account_message.text == values.REGISTER_CREATE_ACCOUNT_MESSAGE

        full_name_title = register_page.get_name_text()
        assert full_name_title.text == values.REGISTER_FULL_NAME_TITLE

        name_textfield = register_page.get_name_textfield()
        assert name_textfield.get_attribute('visible') == values.TRUE_LOWERCASE

        name_instructions_text = register_page.get_name_instructions_text()
        assert name_instructions_text.text == values.REGISTER_FULL_NAME_MESSAGE

        user_name_content = register_page.get_username_text()
        assert user_name_content.text == values.REGISTER_PUBLIC_USERNAME_TITLE

        username_textfield = register_page.get_username_textfield()
        assert username_textfield.get_attribute('visible') == values.TRUE_LOWERCASE

        username_instructions_text = register_page.get_username_instructions_text()
        assert username_instructions_text.text == values.REGISTER_PUBLIC_USERNAME_MESSAGE

        email_text = register_page.get_email_text()
        assert email_text.text == values.REGISTER_EMAIL_TITLE

        email_textfield = register_page.get_email_textfield()
        assert email_textfield.get_attribute('visible') == values.TRUE_LOWERCASE

        email_instructions_text = register_page.get_email_instructions_text()
        assert email_instructions_text.text == values.REGISTER_EMAIL_MESSAGE

        password_text = register_page.get_password_text()
        assert password_text.text == values.REGISTER_PASSWORD_TITLE

        password_text_field = register_page.get_password_textfield()
        assert password_text_field.get_attribute('visible') == values.TRUE_LOWERCASE

        password_instructions_text = register_page.get_password_instructions_text()
        assert password_instructions_text.text == values.REGISTER_PASSWORD_MESSAGE

        country_text = register_page.get_country_text()
        assert country_text.text == values.REGISTER_COUNTRY_TITLE

        country_textfield = register_page.get_country_textfield()
        assert country_textfield

        country_instructions_text = register_page.get_country_instructions_text()
        assert country_instructions_text.text == values.REGISTER_COUNTRY_MESSAGE

        show_optional_fields = register_page.get_show_optional_fields()
        assert show_optional_fields.text == values.REGISTER_SHOW_OPTIONAL_FIELDS

        register_button = register_page.get_create_account_button()
        assert register_button.text == values.REGISTER_CREATE_ACCOUNT_BUTTON

        social_auth_title_text = register_page.get_social_auth_title_text()
        assert social_auth_title_text.text == values.REGISTER_OPTIONS_TITLE

        google_signin = ios_login.get_signin_social_auth_google_button()
        assert google_signin.text == values.REGISTER_GOOGLE_SIGNUP

        facebook_signin = ios_login.get_signin_social_auth_facebook_button()
        assert facebook_signin.text == values.REGISTER_FACEBOOK_SIGNUP

        microsoft_signin =ios_login.get_signin_social_auth_microsoft_button()
        assert microsoft_signin.text == values.REGISTER_MICROSOFT_SIGNUP

        apple_signin = ios_login.get_signin_social_auth_apple_button()
        assert apple_signin.text == values.REGISTER_APPLE_SIGNUP

        name_textfield.send_keys(full_name)
        username_textfield.send_keys(user_name)
        email_textfield.click()
        email_textfield.send_keys(email)

        password_field = register_page.get_password_textfield()
        password_field.send_keys(global_contents.login_password)

        global_contents.scroll_screen(set_capabilities, register_button, name_textfield)
        country_textfield.click()
        picker_title_text = register_page.get_picker_title_text()
        assert picker_title_text.text == values.REGISTER_COUNTRY_PICKER_TITLE

        country_field = register_page.select_country()
        assert country_field.text == values.REGISTER_COUNTRY_SEARCH_FIELD
        country_field.click()
        country_field.send_keys(values.REGISTER_COUNTRY_SELECT)
        accept_button = register_page.get_picker_accept_button()
        assert accept_button.text == values.REGISTER_COUNTRY_ACCEPT_BUTTON
        accept_button.click()
        country_textfield = register_page.get_country_textfield()
        assert country_textfield.text == values.REGISTER_COUNTRY_SELECT

        register_button.click()
        password_instructions_text = register_page.get_password_instructions_text()
        assert password_instructions_text.text == values.REGISTER_PASSWORD_ERROR
