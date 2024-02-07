"""
    New Landing Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import values
from tests.common.globals import Globals


class TestAndroidSignIn:
    """
    Sign in screen's Test Case
    """

    def test_start_sign_in_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify sign in screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidSignIn.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)

        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_signin_button()
        assert android_landing.load_signin_screen().text == values.LOGIN

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """

        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        android_landing.get_back_button().click()
        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.load_signin_screen().text == values.LOGIN
        assert android_sign_in.get_sign_in_description().text == values.SIGN_IN_MESSAGE
        assert android_sign_in.get_sign_in_email_label().text == values.REGISTER_EMAIL_TITLE
        email_field = android_sign_in.get_sign_in_tf_email()
        assert email_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        email_field.send_keys(global_contents.login_user_name)

        assert android_sign_in.get_sign_in_password_label().text == values.PASSWORD
        password_field = android_sign_in.get_sign_in_password_field()
        assert password_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        password_field.send_keys(global_contents.login_password)

        assert android_sign_in.get_signin_button().get_attribute('clickable') == values.TRUE_LOWERCASE

        assert android_sign_in.get_google_auth_button().text == values.GOOGLE_SIGNIN
        assert android_sign_in.get_facebook_auth_button().text == values.FACEBOOK_SIGNIN
        assert android_sign_in.get_microsoft_auth_button().text == values.MICROSOFT_SIGNIN

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

        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        forgot_password_button = android_sign_in.get_sign_in_forgot_password()
        assert forgot_password_button.text == values.FORGOT_PASSWORD
        forgot_password_button.click()
        assert android_landing.get_back_button()
        assert android_landing.get_screen_title().text == values.FORGOT_PASSWORD_TITLE
        assert android_sign_in.get_forgot_password_title().text == values.FORGOT_PASSWORD_TITLE
        assert android_sign_in.get_sign_in_email_label().text == values.FORGOT_EMAIL_TITLE
        email_field = android_sign_in.get_sign_in_tf_email()
        assert email_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        random_email = global_contents.generate_random_credentials(8)
        email_field.send_keys(random_email + '@yop.com')

        reset_button = android_sign_in.get_forgot_password_reset_button()
        assert reset_button.text == values.RESET_PASSWORD_BUTTON
        reset_button.click()

        sign_in_button = android_sign_in.get_all_textviews()[3]
        assert sign_in_button.text == values.LOGIN
        sign_in_button.click()
        assert android_sign_in.get_sign_in_description().text == values.SIGN_IN_MESSAGE
