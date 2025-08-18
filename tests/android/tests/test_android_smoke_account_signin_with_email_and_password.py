"""Android - SMOKE - Registration with Email and Password"""

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
@allure.story("user can only sign in with valid email and password")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_ACCOUNTS
@pytest.mark.ANDROID_SMOKE
class TestAccountSignInWithEmailAndPassword:
    """Test Account Sign In with Email and Password"""

    def test_account_signin_with_email_and_password(self, set_capabilities, setup_logging):
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
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.SIGN_IN_TEXT)

        with allure.step("Enter a valid email or username"):
            assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)

        with allure.step("Enter a valid password"):
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
            expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)

        with allure.step("Click on Log out button on the confirmation prompt"):
            assert profile_page.logout_prompt_logout_button_text.click()
            assert android_landing.signin_button.exists()
