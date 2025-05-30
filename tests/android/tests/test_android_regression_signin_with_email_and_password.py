"""Android - Regression - Registration with Email and Password"""

from time import sleep

import allure
import pytest

from framework import Element, expect
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.globals import Globals


@allure.epic("Accounts")
@allure.feature("Sign In")
@allure.story("Sign In with email and password")
@allure.link("https://2u-internal.atlassian.net/browse/LEARNER-10489", name="LEARNER-10489")
@allure.suite("REGRESSION")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_REGRESSION
class TestAccountSignInWithEmailAndPassword:
    """Test Account Sign In with Email and Password"""

    @pytest.mark.parametrize(
        "invalid_user_id, unregistered_user_id", [("john doe", "johndoe"), ("abc@gmail", "abc001188@gmail.com")]
    )
    def test_account_signin_with_email_and_password(
        self, set_capabilities, setup_logging, invalid_user_id, unregistered_user_id
    ):
        """
        Verify sign in flow with email and password
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()
        android_sign_in = AndroidSignIn()
        whats_new_page = AndroidWhatsNew()
        global_contents = Globals(setup_logging)

        with allure.step("verify “Sign in“ button exists on landing page"):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            assert android_landing.signin_button.exists()

        with allure.step("Click on Sign in button"):
            assert android_landing.load_signin_screen()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)
            expect(android_sign_in.sign_in_description).to_have(values.SIGN_IN_MESSAGE)

        with allure.step("verify the Email and password field headings texts"):
            expect(android_sign_in.sign_in_email_label).to_have(values.EMAIL_OR_USERNAME)
            expect(android_sign_in.sign_in_tf_email).to_be_clickable()
            expect(android_sign_in.sign_in_password_label).to_have(values.PASSWORD)
            expect(android_sign_in.sign_in_password_field).to_be_clickable()

        with allure.step("verify social login buttons are enabled"):
            expect(android_sign_in.google_auth_button).to_be_enabled()
            expect(android_sign_in.get_facebook_auth_button).to_be_enabled()
            expect(android_sign_in.get_microsoft_auth_button).to_be_enabled()

        with allure.step("Leave all fields empty and click on Sign In button"):
            assert android_sign_in.signin_button.click()
            expect(android_sign_in.email_field_error).to_have(
                "Please enter your username or e-mail address and try again."
            )
            expect(android_sign_in.password_field_error).to_have("Please enter your password and try again.")

        with allure.step("Enter invalid Username/email with valid password"):
            assert android_sign_in.sign_in_tf_email.send_keys(invalid_user_id)
            assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)

        with allure.step("Click on Sign in button"):
            assert android_sign_in.signin_button.click()

        with allure.step("Invalid credentials toast appear at the bottom"):
            assert android_sign_in.find_by_text_on_screen("Invalid email or username")

        with allure.step("Enter a valid, unregistered username/email with correct password"):
            assert android_sign_in.sign_in_tf_email.clear()
            assert android_sign_in.sign_in_tf_email.send_keys(unregistered_user_id)

        with allure.step("Click on Sign in button"):
            assert android_sign_in.signin_button.click()

        with allure.step("Invalid credentials toast appear at the bottom"):
            assert android_sign_in.find_by_text_on_screen("Invalid credentials")

        with allure.step("Clear out the email/username field and verify error message"):
            assert android_sign_in.sign_in_tf_email.clear()

        with allure.step("Click on Sign in button"):
            assert android_sign_in.signin_button.click()

        with allure.step("error appears under email field"):
            expect(android_sign_in.email_field_error).to_have(
                "Please enter your username or e-mail address and try again."
            )

        with allure.step("Enter a valid username, clear out the password field"):
            assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)
            assert android_sign_in.sign_in_password_field.clear()
            assert android_sign_in.signin_button.click()

        with allure.step("error appears under password field"):
            expect(android_sign_in.password_field_error).to_have("Please enter your password and try again.")

        with allure.step("Enter an invalid password and hit sign in button"):
            assert android_sign_in.sign_in_password_field.send_keys("12900000")
            assert android_sign_in.signin_button.click()

        with allure.step("Invalid credentials toast appear at the bottom"):
            assert android_sign_in.find_by_text_on_screen("Invalid credentials")

        with allure.step("verify eye icon on password field is enabled"):
            expect(android_sign_in.show_password_eye_icon).to_be_enabled()

        with allure.step("Enter a valid password"):
            assert android_sign_in.sign_in_password_field.clear()
            sleep(3)
            assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)

        with allure.step("Click on Sign in button"):
            assert android_sign_in.signin_button.click()
            setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")
            if whats_new_page.get_close_button.exists(raise_exception=False):
                assert whats_new_page.get_close_button.click()

        with allure.step("Goto Profile Tab"):
            assert main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            expect(profile_page.profile_username).to_have(f"@{global_contents.login_user_name}")
            expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)

        with allure.step("Click on Settings icon"):
            assert profile_page.settings_button.click()
            profile_page.get_profile_txt_terms_of_use.scroll_vertically_from_element()

        with allure.step("Click on Log out button"):
            assert profile_page.profile_txt_logout.click()
            expect(profile_page.logout_dialogue_title).to_have("Are you sure you want to log out?")
            expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)

        with allure.step("Click on Log out button on the confirmation prompt"):
            assert profile_page.logout_prompt_logout_button_text.click()
            assert android_landing.signin_button.exists()

        with allure.step("Click on Sign in button"):
            assert android_landing.load_signin_screen()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)

        with allure.step("Enter a valid email"):
            assert android_sign_in.sign_in_tf_email.send_keys("automation-user007@yopmail.com")

        with allure.step("Enter a valid password"):
            assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)

        with allure.step("Click on Sign in button"):
            assert android_sign_in.signin_button.click()
            setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")

        with allure.step("Goto Profile Tab"):
            assert main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            expect(profile_page.profile_username).to_have(f"@{global_contents.login_user_name}")
            expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)

        with allure.step("Click on Settings icon"):
            assert profile_page.settings_button.click()
            profile_page.get_profile_txt_terms_of_use.scroll_vertically_from_element()

        with allure.step("Click on Log out button"):
            assert profile_page.profile_txt_logout.click()
            expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)

        with allure.step("Click on Log out button on the confirmation prompt"):
            assert profile_page.logout_prompt_logout_button_text.click()
            assert android_landing.signin_button.exists()
