"""
    Register Screen Test Module
"""

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_register import IosRegister


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
        user_name = global_contents.generate_random_credentials(5)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + ' ' + last_name
        password = global_contents.generate_random_credentials(8)

        assert register_page.get_register_screen_heading().text == values.REGISTER

        all_static_text = global_contents.get_ios_all_static_text(set_capabilities)
        sign_up_heading = all_static_text[1]
        assert sign_up_heading.text == values.REGISTER_SIGN_UP_HEADING

        create_account_message = all_static_text[2]
        assert create_account_message.text == values.REGISTER_CREATE_ACCOUNT_MESSAGE

        full_name_title = all_static_text[3]
        assert full_name_title.text == values.REGISTER_FULL_NAME_TITLE

        full_name_content = all_static_text[4]
        assert full_name_content.text == values.REGISTER_FULL_NAME_MESSAGE

        public_name_title = all_static_text[5]
        assert public_name_title.text == values.REGISTER_PUBLIC_USERNAME_TITLE

        public_name_content = all_static_text[6]
        assert public_name_content.text == values.REGISTER_PUBLIC_USERNAME_MESSAGE

        email_title = all_static_text[7]
        assert email_title.text == values.REGISTER_EMAIL_TITLE

        email_message = all_static_text[8]
        assert email_message.text == values.REGISTER_EMAIL_MESSAGE

        password_title = all_static_text[9]
        assert password_title.text == values.REGISTER_PASSWORD_TITLE

        password_message = all_static_text[10]
        assert password_message.text == values.REGISTER_PASSWORD_MESSAGE

        country_title = all_static_text[11]
        assert country_title.text == values.REGISTER_COUNTRY_TITLE

        country_message = all_static_text[12]
        assert country_message.text == values.REGISTER_COUNTRY_MESSAGE

        all_textfields = global_contents.get_ios_all_editfields(set_capabilities)
        full_user_name = all_textfields[0]
        full_user_name.send_keys(full_name)

        public_user_name = all_textfields[1]
        public_user_name.send_keys(user_name)

        email_field = all_textfields[2]
        email_field.send_keys(email)
        email_title.click()

        global_contents.scroll_screen(set_capabilities, email_field, full_name_title)

        register_page.get_password_field().send_keys(password)
        password_message.click()

        all_buttons = global_contents.get_ios_all_buttons(set_capabilities)
        create_account_button = all_buttons[2]
        assert create_account_button.text == values.REGISTER_CREATE_ACCOUNT_BUTTON

        google_register = all_buttons[3]
        assert google_register.text == values.REGISTER_GOOGLE_SIGNIN

        register_facebook = all_buttons[4]
        assert register_facebook.text == values.REGISTER_FACEBOOK_SIGNIN

        register_microsoft = all_buttons[5]
        assert register_microsoft.text == values.REGISTER_MICROSOFT_SIGNIN

        register_apple = all_buttons[6]
        assert register_apple.text == values.REGISTER_APPLE_SIGNIN
