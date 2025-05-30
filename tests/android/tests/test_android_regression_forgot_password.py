"""
New Landing Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import utils, values


@allure.epic("Accounts")
@allure.feature("Account Recovery")
@allure.story("Forgot password")
@allure.link("https://2u-internal.atlassian.net/browse/LEARNER-10514", name="LEARNER-10514")
@allure.suite("REGRESSION")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_REGRESSION
class TestAndroidForgotPassword:
    """
    Sign in screen's Test Case
    """

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()

        with allure.step("Click on Sign in Button"):
            assert android_landing.signin_button.click()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)
            expect(android_sign_in.sign_in_description).to_have(values.SIGN_IN_MESSAGE)
            expect(android_sign_in.forgot_password_button).to_have(values.FORGOT_PASSWORD)

        with allure.step("Click on Forgot password button"):
            assert android_sign_in.forgot_password_button.click()
            expect(android_sign_in.screen_title).to_have(values.FORGOT_PASSWORD_TITLE)
            expect(android_sign_in.forgot_password_title).to_have(values.FORGOT_PASSWORD_TITLE)
            expect(android_sign_in.forgot_password_email_label).to_have(values.FORGOT_EMAIL_TITLE)
            expect(android_sign_in.forgot_password_email_placeholder).to_have("username@domain.com")
            assert android_sign_in.forgot_password_reset_button.exists()
            expect(android_sign_in.forgot_password_reset_button_label).to_have(values.RESET_PASSWORD_BUTTON)

        with allure.step("Click reset password button"):
            assert android_sign_in.forgot_password_reset_button.click()
            expect(android_sign_in.email_field_error).to_have(values.FORGOT_PASSWORD_EMAIL_ERROR)

        with allure.step("Click on email field & enter random email “test_user@yopmail.com”"):
            random_email = utils.generate_random_credentials(8) + "@yopmail.com"
            assert android_sign_in.sign_in_tf_email.send_keys(random_email)

        with allure.step("Click reset password button"):
            assert android_sign_in.forgot_password_reset_button.click()
            assert android_sign_in.find_by_text_on_screen(
                f"We have sent a password recover instructions to your email {random_email}"
            )
            assert android_sign_in.find_by_text_on_screen(values.FORGOT_RECOVER_TITLE_TEXT)
            expect(android_sign_in.password_recovery_sign_in_btn).to_have(values.LOGIN)

        with allure.step("Click on Sign in button"):
            assert android_sign_in.password_recovery_sign_in_btn.click()
            expect(android_sign_in.sign_in_description).to_have(values.SIGN_IN_MESSAGE)
