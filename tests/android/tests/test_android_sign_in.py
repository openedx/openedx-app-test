"""
New Landing Test Module
"""

from framework import expect
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import utils, values
from tests.common.globals import Globals
from framework.element import Element


class TestAndroidSignIn:
    """
    Sign in screen's Test Case
    """

    def test_start_sign_in_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify sign in screen is loaded successfully
        """

        setup_logging.info(f"Starting {TestAndroidSignIn.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()

        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        assert android_landing.signin_button.exists()
        assert android_landing.load_signin_screen()
        expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen
            "Back icon", "Sign In" Title, "Username or e-mail address" label, Username edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()
        global_contents = Globals(setup_logging)

        global_contents.get_back_button(set_capabilities).click()
        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        assert android_landing.signin_button.exists()
        assert android_landing.load_signin_screen()
        expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)
        expect(android_sign_in.sign_in_email_label).to_have(values.EMAIL_OR_USERNAME)
        expect(android_sign_in.sign_in_tf_email).to_be_clickable()
        assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)
        expect(android_sign_in.sign_in_password_label).to_have(values.PASSWORD)
        expect(android_sign_in.sign_in_password_field).to_be_clickable()
        assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)
        expect(android_sign_in.signin_button).to_be_clickable()
        expect(android_sign_in.google_auth_button).to_be_enabled()
        expect(android_sign_in.get_facebook_auth_button).to_be_enabled()
        expect(android_sign_in.get_microsoft_auth_button).to_be_enabled()

    def test_forgot_password_alert(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify tapping 'Forgot password?' will  load 'Reset Password' screen
            Verify following contents are visible on 'Reset Password' alert,
            Alert Title, Alert Message, Email edit field, 'Reset Password' button
            Verify that check your email screen is shown after entering email
            Verify signin button is shown in check email screen
            Verify signin button will load 'Sign In' screen
        """

        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()

        expect(android_sign_in.forgot_password_button).to_have(values.FORGOT_PASSWORD)
        assert android_sign_in.forgot_password_button.click()
        assert android_sign_in.back_navigation_button.exists()
        expect(android_landing.screen_title).to_have(values.FORGOT_PASSWORD_TITLE)
        expect(android_sign_in.forgot_password_title).to_have(values.FORGOT_PASSWORD_TITLE)
        expect(android_sign_in.sign_in_email_label).to_have(values.FORGOT_EMAIL_TITLE)
        expect(android_sign_in.sign_in_tf_email).to_be_clickable()
        assert android_sign_in.forgot_password_reset_button.click()
        expect(android_sign_in._forgot_password_email_error).to_have(values.FORGOT_EMAIL_ERROR)
        random_email = utils.generate_random_credentials(8)
        assert android_sign_in.sign_in_tf_email.send_keys(random_email + "@yop.com")
        expect(android_sign_in.forgot_password_reset_button).to_be_displayed()
        expect(android_sign_in.forgot_password_reset_button).to_have(values.RESET_PASSWORD_BUTTON)
        assert android_sign_in.forgot_password_reset_button.click()
        android_sign_in.verify_password_recovery_prompts(random_email + "@yop.com")
        expect(android_sign_in.password_recovery_sign_in_btn).to_have(values.LOGIN)
        assert android_sign_in.password_recovery_sign_in_btn.click()
        expect(android_sign_in.sign_in_description).to_have(values.SIGN_IN_MESSAGE)
