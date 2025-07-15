"""iOS - SMOKE - Forgot Password"""

import allure
import pytest

from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin


@allure.epic("Accounts")
@allure.feature("Account Recovery")
@allure.story("Forgot password")
@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestAccountForgotPassword:
    """Test class for iOS - SMOKE - Forgot Password"""

    def test_account_forgot_password(self, set_capabilities, setup_logging):
        """
        Verify forgot password flow
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_login = IosLogin()
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding()
        random_email = f"{global_contents.generate_random_credentials(8)}@yop.com"

        with allure.step("Click on Sign in Button"):
            if ios_landing.allow_notifications_button.exists(raise_exception=False):
                ios_landing.allow_notifications_button.click()
            sign_in_button = ios_landing.sign_in_button
            expect(sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            expect(ios_login.signin_welcome_text).to_have(values.SIGN_IN_MESSAGE, ElementAttribute.LABEL)
            expect(ios_login.get_signin_forgot_password_button).to_have(values.FORGOT_PASSWORD, ElementAttribute.LABEL)

        with allure.step("Click on forgot password button"):
            ios_login.get_signin_forgot_password_button.click()
            expect(ios_login.screen_heading_title).to_have(values.FORGOT_PASSWORD_SCREEN_TITLE, ElementAttribute.LABEL)
            expect(ios_login.forgot_title_text).to_have(values.FORGOT_PASSWORD_TITLE, ElementAttribute.LABEL)
            expect(ios_login.forgot_email_text_field_label).to_have(values.FORGOT_EMAIL_TITLE, ElementAttribute.LABEL)
            expect(ios_login.forgot_email_textfield_placeholder).to_have(
                values.FORGOT_EMAIL_TEXT_FIELD_PLACEHOLDER, ElementAttribute.LABEL
            )
            expect(ios_login.forgot_description_text).to_have(values.FORGOT_DESCRIPTION_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on email field & enter random email"):
            ios_login.forgot_email_textfield.click()
            ios_login.forgot_email_textfield.send_keys(random_email)

        with allure.step("Click reset password button"):
            reset_password_button = ios_login.reset_password_button
            expect(reset_password_button).to_have(values.RESET_PASSWORD_BUTTON, ElementAttribute.LABEL)
            reset_password_button.click()
            expect(ios_login.forgot_recover_title_text).to_have(
                values.FORGOT_RECOVER_TITLE_TEXT, ElementAttribute.LABEL
            )
            expect(ios_login.forgot_check_email_image).to_have(values.FORGOT_CHECK_EMAIL_IMAGE, ElementAttribute.LABEL)
            recovery_description_label = f"{values.FORGOT_RECOVER_DESCRIPTION} {random_email}"
            expect(ios_login.forgot_recover_description_text).to_have(
                recovery_description_label, ElementAttribute.LABEL
            )
            sign_in_button = ios_login.signin_button
            expect(ios_login.signin_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            sign_in_button.click()
            logo_image = ios_landing.edx_logo_image
            expect(logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            setup_logging.info("Ending Test Case")
