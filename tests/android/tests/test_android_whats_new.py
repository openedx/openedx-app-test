"""
    Whats New Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestAndroidWhatsNew:
    """
    Whats new screen's Test Case
    """

    def test_start_whats_new_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidWhatsNew.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if global_contents.whats_new_enable:
            assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
            assert android_landing.get_signin_button()
            assert android_landing.load_signin_screen().text == values.LOGIN

            assert android_sign_in.get_sign_in_email_label().text == values.EMAIL_OR_USERNAME
            email_field = android_sign_in.get_sign_in_tf_email()
            assert email_field.get_attribute('clickable') == values.TRUE_LOWERCASE
            email_field.send_keys(global_contents.login_user_name)

            assert android_sign_in.get_sign_in_password_label().text == values.PASSWORD
            password_field = android_sign_in.get_sign_in_password_field()
            assert password_field.get_attribute('clickable') == values.TRUE_LOWERCASE
            password_field.send_keys(global_contents.login_password)
            assert android_sign_in.get_signin_button().get_attribute('clickable') == values.TRUE_LOWERCASE
            android_sign_in.get_signin_button().click()
        else:
            setup_logging.info('Whats New feature is not enabled')

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen 
                "Screen Title", "Cross Icon", "Main Feature Image",
                    "Feature Title", "Feature Details", "Done"
            Verify all screen contents have their default values
        """

        android_landing = AndroidLanding(set_capabilities, setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if global_contents.whats_new_enable:
            close_btn = whats_new_page.get_close_button()
            assert close_btn.get_attribute('clickable') == values.TRUE_LOWERCASE

            assert android_landing.get_screen_title().text == values.WHATS_NEW_TITLE
            assert whats_new_page.get_whats_new_msg_title().text
            assert whats_new_page.get_whats_new_description().text
            assert whats_new_page.get_next_btn()

            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_done_button().click()
        else:
            setup_logging.info('Whats New feature is not enabled')
