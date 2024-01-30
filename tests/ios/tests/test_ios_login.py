"""
    Login Test Module
"""

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_landing import IosLanding


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
        ios_landing = IosLanding(set_capabilities, setup_logging)
        ios_login = IosLogin(set_capabilities, setup_logging)

        sign_in_button = ios_landing.get_sign_in_button()
        assert ios_landing.get_sign_in_button().text == values.LOGIN
        sign_in_button.click()
        sign_in_title = ios_login.get_sign_in_title()
        assert sign_in_title.text == values.LOGIN

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen, 
                "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
                Password edit-field, "Forgot your password?" option, "Sign In" button,
                "Or sing in with" label, "Facebook" button, "Google" button
            Verify all screen contents have their default values
        """

        ios_login = IosLogin(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        sign_in_title = ios_login.get_sign_in_title()
        assert sign_in_title.text == values.LOGIN

        sign_in_message = ios_login.get_signin_welcome_text()
        assert sign_in_message.text == values.SIGN_IN_MESSAGE

        email_or_username_title = ios_login.get_signin_username_text()
        assert email_or_username_title.text == values.EMAIL_OR_USERNAME

        email_field = ios_login.get_signin_username_textfield()
        assert email_field.text == values.EMAIL_OR_USERNAME
        email_field.send_keys(global_contents.login_user_name)

        password_title = ios_login.get_signin_password_text()
        assert password_title.text == values.PASSWORD
        password_title.click()
        password_field = ios_login.get_signin_password_textfield()
        assert password_field.get_attribute('value') == values.PASSWORD
        password_field.send_keys(global_contents.login_password)
        password_title.click()

        sign_in_button = ios_login.get_signin_button()
        assert sign_in_button.text == values.LOGIN

        global_contents.scroll_from_element(set_capabilities, sign_in_button)

        social_auth_title = ios_login.get_signin_social_auth_title_text()
        social_auth_title.text == values.SOCIAL_AUTH_TITLE

        google_signin = ios_login.get_signin_social_auth_google_button()
        assert google_signin.text == values.GOOGLE_SIGNIN

        facebook_signin = ios_login.get_signin_social_auth_facebook_button()
        assert facebook_signin.text == values.FACEBOOK_SIGNIN

        microsoft_signin =ios_login.get_signin_social_auth_microsoft_button()
        assert microsoft_signin.text == values.MICROSOFT_SIGNIN

        apple_signin = ios_login.get_signin_social_auth_apple_button()
        assert apple_signin.text == values.APPLE_SIGNIN

    def test_forgot_password_alert_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping 'Forgot password?' will  load 'Reset Password' screen
            Verify following contents are visible on 'Reset Password' alert, 
            Alert Title, Alert Message, Email edit field, 'Reset Password' button
            Verify that check your email screen is shown after entering email
            Verify signin button is shown in check email screen
            Verify signin button will load 'Sign In' screen
        """

        ios_login = IosLogin(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        forgot_password_button = ios_login.get_signin_forgot_password_button()
        assert forgot_password_button.text == values.FORGOT_PASSWORD

        forgot_password_button.click()
        heading_title = global_contents.get_screen_heading_title(set_capabilities)
        assert heading_title.text == values.FORGOT_PASSWORD_TITLE

        title_text = ios_login.get_forgot_title_text()
        assert title_text.text == values.FORGOT_PASSWORD_TITLE

        description_text = ios_login.get_forgot_description_text()
        assert description_text.text == values.FORGOT_DESCRIPTION_TEXT

        email_text = ios_login.get_forgot_email_text()
        assert email_text.text == values.FORGOT_EMAIL_TITLE

        email_textfield = ios_login.get_forgot_email_textfield()
        assert email_textfield.text == values.FORGOT_EMAIL_TITLE
        email_textfield.click()
        random_email = global_contents.generate_random_credentials(8)
        email_textfield.send_keys(random_email + '@yop.com')

        reset_password_button = ios_login.get_forgot_reset_password_button()
        assert reset_password_button.text == values.RESET_PASSWORD_BUTTON
        reset_password_button.click()

        check_email_image = ios_login.get_forgot_check_email_image()
        assert check_email_image.text == values.FORGOT_CHECK_EMAIL_IMAGE

        recover_title_text = ios_login.get_forgot_recover_title_text()
        assert recover_title_text.text == values.FORGOT_RECOVER_TITLE_TEXT

        recover_description_text = ios_login.get_forgot_recover_description_text()
        assert values.FOROGT_RECOVER_DESCRIPTION in recover_description_text.text

        sign_in_button = ios_login.get_signin_button()
        assert sign_in_button.text == values.LOGIN
        sign_in_button.click()

        logo_image = ios_landing.get_logo_image()
        assert logo_image.text == values.LANDING_LOGO_IMAGE
        setup_logging.info('Ending Test Case')
