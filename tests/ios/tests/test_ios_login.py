"""
Login Test Module
"""

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info("Starting Test Case")
        ios_landing = IosLanding()
        ios_login = IosLogin()

        if ios_landing.allow_notifications_button.exists(raise_exception=False):
            ios_landing.allow_notifications_button.click()

        sign_in_button = ios_landing.sign_in_button
        expect(sign_in_button).to_have(values.LOGIN)
        assert sign_in_button.click()
        expect(ios_login.sign_in_title).to_have(values.LOGIN)

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen,
                "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
                Password edit-field, "Forgot your password?" option, "Sign In" button,
                "Or sing in with" label, "Facebook" button, "Google" button
            Verify all screen contents have their default values
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_login = IosLogin()
        global_contents = Globals(setup_logging)

        expect(ios_login.sign_in_title).to_have(values.LOGIN)
        expect(ios_login.signin_welcome_text).to_have(values.SIGN_IN_MESSAGE)
        expect(ios_login.signin_username_text).to_have(values.EMAIL_OR_USERNAME_IOS)
        expect(ios_login.signin_username_textfield).to_have(values.EMAIL_OR_USERNAME_IOS)
        assert ios_login.signin_username_textfield.send_keys(global_contents.login_user_name)

        password_title = ios_login.signin_password_text
        expect(password_title).to_have(values.PASSWORD)
        assert password_title.click()
        password_field = ios_login.signin_password_textfield
        expect(password_field).to_have(values.PASSWORD, ElementAttribute.VALUE)
        assert password_field.send_keys(global_contents.login_password)
        assert password_title.click()

        sign_in_button = ios_login.signin_button
        expect(ios_login.signin_button).to_have(values.LOGIN)
        sign_in_button.scroll_vertically_from_element()
        expect(ios_login.signin_social_auth_title_text).to_have(values.SOCIAL_AUTH_TITLE)
        expect(ios_login.signin_social_auth_google_button).to_have(values.GOOGLE_SIGNIN)
        expect(ios_login.signin_social_auth_facebook_button).to_have(values.FACEBOOK_SIGNIN)
        expect(ios_login.signin_social_auth_microsoft_button).to_have(values.MICROSOFT_SIGNIN)
        expect(ios_login.signin_social_auth_apple_button).to_have(values.APPLE_SIGNIN)

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_login = IosLogin()
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding()

        expect(ios_login.get_signin_forgot_password_button).to_have(values.FORGOT_PASSWORD)
        assert ios_login.get_signin_forgot_password_button.click()
        expect(ios_login.screen_heading_title).to_have(values.FORGOT_PASSWORD_TITLE)
        expect(ios_login.forgot_title_text).to_have(values.FORGOT_PASSWORD_TITLE)
        description_text = ios_login.forgot_description_text
        expect(description_text).to_have(values.FORGOT_DESCRIPTION_TEXT)
        email_text = ios_login.forgot_email_text_field_label
        expect(email_text).to_have(values.FORGOT_EMAIL_TITLE)
        email_textfield = ios_login.forgot_email_textfield
        expect(ios_login.forgot_email_textfield_placeholder).to_have(values.FORGOT_EMAIL_TEXT_FIELD_PLACEHOLDER)
        email_textfield.click()
        random_email = global_contents.generate_random_credentials(8)
        email_textfield.send_keys(random_email + "@yop.com")
        reset_password_button = ios_login.forgot_reset_password_button
        expect(reset_password_button).to_have(values.RESET_PASSWORD_BUTTON)
        assert reset_password_button.click()
        expect(ios_login.forgot_check_email_image).to_have(values.FORGOT_CHECK_EMAIL_IMAGE)
        expect(ios_login.forgot_recover_title_text).to_have(values.FORGOT_RECOVER_TITLE_TEXT)
        expect(ios_login.forgot_recover_description_text).to_contain(values.FORGOT_RECOVER_DESCRIPTION)
        sign_in_button = ios_login.signin_button
        expect(ios_login.signin_button).to_have(values.LOGIN)
        assert sign_in_button.click()
        logo_image = ios_landing.get_logo_image
        expect(logo_image).to_have(values.LANDING_LOGO_IMAGE)
        setup_logging.info("Ending Test Case")
