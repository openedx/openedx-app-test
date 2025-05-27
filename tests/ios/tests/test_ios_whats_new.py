"""
What's New Test Module
"""

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.enums.general_enums import IosClassViews
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f"Starting {TestIosWhatsNew.__name__} Test Case")
        ios_landing = IosLanding()
        ios_login = IosLogin()
        global_contents = Globals(setup_logging)

        if ios_landing.allow_notifications_button.exists(raise_exception=False):
            ios_landing.allow_notifications_button.click()

        if global_contents.whats_new_enable:
            sign_in_button = ios_landing.sign_in_button
            expect(sign_in_button).to_have(values.LOGIN)
            sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.LOGIN)
            expect(ios_login.username_text_field_placeholder).to_have(values.EMAIL_OR_USERNAME_IOS)
            ios_login.username_textfield.send_keys(global_contents.login_user_name + "\n")
            expect(ios_login.password_text_field_label).to_have(values.PASSWORD, ElementAttribute.LABEL)
            ios_login.password_textfield.send_keys(global_contents.login_password + "\n")
            expect(ios_login.signin_button).to_have(values.LOGIN, ElementAttribute.LABEL)
            ios_login.signin_button.click()
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        whats_new_page = IosWhatsNew()
        global_contents = Globals(setup_logging)

        if global_contents.whats_new_enable:
            close_btn = whats_new_page.close_button
            expect(close_btn).to_have(values.WHATS_NEW_CLOSE_BUTTON)
            screen_title = IosWhatsNew.find_all_views_on_screen(IosClassViews.STATIC_TEXT)[0]
            expect(screen_title).to_have(values.WHATS_NEW_TITLE)
            expect(whats_new_page.get_whats_new_msg_title).to_match(r".+")
            expect(whats_new_page.get_whats_new_description).to_match(r".+")
            next_button = whats_new_page.whats_new_next_button
            expect(next_button).to_have(values.WHATS_NEW_NEXT_BUTTON)
            expect(whats_new_page.navigate_features()).to_have("Done", ElementAttribute.LABEL)
            assert whats_new_page.whats_new_next_button.click()
        else:
            setup_logging.info("Whats New feature is not enabled")
