"""
    What's New Test Module
"""

from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_whats_new import IosWhatsNew


class TestIosWhatsNew:
    """
    What's new screen's Test Case
    """

    def test_start_whats_new_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify What's New screen is loaded successfully
        """

        setup_logging.info(f"Starting {TestIosWhatsNew.__name__} Test Case")
        ios_landing = IosLanding(set_capabilities, setup_logging)
        ios_login = IosLogin(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()

        if global_contents.whats_new_enable:
            sign_in_button = ios_landing.get_sign_in_button()
            assert ios_landing.get_sign_in_button().text == values.LOGIN
            sign_in_button.click()
            sign_in_title = ios_login.get_sign_in_title()
            assert sign_in_title.text == values.LOGIN

            email_field = ios_login.get_signin_username_textfield()
            assert email_field.text == values.EMAIL_OR_USERNAME_IOS
            email_field.send_keys(global_contents.login_user_name)

            password_title = ios_login.get_signin_password_text()
            assert password_title.text == values.PASSWORD
            password_title.click()
            password_field = ios_login.get_signin_password_textfield()
            assert password_field.get_attribute("value") == values.PASSWORD
            password_field.send_keys(global_contents.login_password)
            password_title.click()
            sign_in_button = ios_login.get_signin_button()
            assert sign_in_button.text == values.LOGIN
            sign_in_button.click()
        else:
            setup_logging.info("Whats New feature is not enabled")

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen
                "Screen Title", "Cross Icon", "Main Feature Image",
                    "Feature Title", "Feature Details", "Done"
            Verify all screen contents have their default values
        """

        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if global_contents.whats_new_enable:
            close_btn = whats_new_page.get_close_button()
            assert close_btn.text == values.WHATS_NEW_CLOSE_BUTTON

            screen_title = global_contents.get_ios_all_static_text(set_capabilities)[0]
            assert screen_title.text == values.WHATS_NEW_TITLE
            assert whats_new_page.get_whats_new_msg_title().text
            assert whats_new_page.get_whats_new_description().text
            next_button = whats_new_page.get_next_btn()
            assert next_button.text == values.WHATS_NEW_NEXT_BUTTON
            assert whats_new_page.navigate_features().text == "Done"
            whats_new_page.get_next_btn().click()
        else:
            setup_logging.info("Whats New feature is not enabled")
