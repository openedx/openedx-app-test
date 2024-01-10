"""
    Login Test Module
"""

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin


class TestIosLogin:
    """
    Login screen's Test Case
    """

    def test_load_login_screen(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Login screen is loaded successfully
        """

        setup_logging.info('Starting Test Case')
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        sign_in_button = ios_login_page.get_sign_in_button()
        assert ios_login_page.get_sign_in_button().text == values.LOGIN
        sign_in_button.click()

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen, 
                "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
                Password edit-field, "Forgot your password?" option, "Sign In" button,
                "Or sing in with" label, "Facebook" button, "Google" button
            Verify all screen contents have their default values
        """

        ios_login_page = IosLogin(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        all_static_text = global_contents.get_ios_all_static_text(set_capabilities)
        sign_in_heading = all_static_text[0]
        assert sign_in_heading.text == values.LOGIN

        sign_in_message = all_static_text[1]
        assert sign_in_message.text == values.SIGN_IN_MESSAGE

        email_or_username_title = all_static_text[2]
        assert email_or_username_title.text == values.EMAIL_OR_USERNAME

        email_field = global_contents.get_ios_all_editfields(set_capabilities)[0]
        assert email_field.text == values.EMAIL_OR_USERNAME
        email_field.send_keys(global_contents.login_user_name)

        password_title = all_static_text[3]
        assert password_title.text == values.PASSWORD
        password_title.click()
        password_field = ios_login_page.get_password_field()
        assert password_field.get_attribute('value') == values.PASSWORD
        password_field.send_keys(global_contents.login_password)
        password_title.click()

        sign_in_button = global_contents.get_ios_all_buttons(set_capabilities)[2]
        assert sign_in_button.text == values.LOGIN

        global_contents.scroll_from_element(set_capabilities, sign_in_button)
        all_static_text = global_contents.get_ios_all_buttons(set_capabilities)

        google_signin = all_static_text[3]
        assert google_signin.text == values.GOOGLE_SIGNIN

        facebook_signin = all_static_text[4]
        assert facebook_signin.text == values.FACEBOOK_SIGNIN

        microsoft_signin = all_static_text[5]
        assert microsoft_signin.text == values.MICROSOFT_SIGNIN

        apple_signin = all_static_text[6]
        assert apple_signin.text == values.APPLE_SIGNIN
        setup_logging.info('Ending Test Case')
