"""Android - SMOKE - Registration with Email and Password"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_register import AndroidRegister
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_settings_page import AndroidSettingsPage
from tests.common import values
from tests.common.enums import ElementAttribute, ScrollDirections
from tests.common.enums.general_enums import CountryAbbreviation
from tests.common.globals import Globals


@allure.epic("Accounts")
@allure.feature("Registration")
@allure.story("Registration with email and password")
@allure.link("https://2u-internal.atlassian.net/browse/LEARNER-10485", name="LEARNER-10485")
@pytest.mark.ANDROID_SMOKE
class TestAccountRegistrationWithEmailAndPassword:
    """Test Account Registration with Email and Password"""

    def test_account_registration_with_email_and_password(self, set_capabilities, setup_logging):
        """
        Verify registration flow with email and password
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_register = AndroidRegister()
        main_dashboard = AndroidMainDashboard()
        profile_page = AndroidProfile()
        settings_page = AndroidSettingsPage()
        global_contents = Globals(setup_logging)

        with allure.step("verify 'Register' button exists on landing page"):
            assert android_landing.register_button.exists()
            expect(android_landing.register_button_text).to_have(values.REGISTER)

        with allure.step("Click on Register button"):
            assert android_landing.register_button.click()
            expect(android_register.screen_title).to_have(values.REGISTER)

        with allure.step("Enter Full Name"):
            full_name = global_contents.generate_random_credentials(6)
            android_register.name_text_field.send_keys(full_name)

        with allure.step("Enter a valid username"):
            username = global_contents.generate_random_credentials(6)
            android_register.username_text_field.send_keys(username)

        with allure.step("Enter a valid unregistered email"):
            email = f"{global_contents.generate_random_credentials(6)}@yopmail.com"
            android_register.email_text_field.send_keys(email)

        with allure.step("Enter a valid password"):
            password = global_contents.generate_random_credentials(8) + "123"
            android_register.password_text_field.send_keys(password)
            Element.swipe_vertical_full_page(ScrollDirections.UP)

        with allure.step("Open country/region picker dropdown"):
            android_register.country_text_field.click()
            expect(android_register.get_register_country_selection_dialogue).to_have(
                values.REGISTER_COUNTRY_PICKER_TITLE
            )

        with allure.step("Search for a country and select it"):
            android_register.sb_search_field.send_keys(values.REGISTER_COUNTRY)
            assert Globals.get_country_by_resource_id(CountryAbbreviation.US).click()
            expect(android_register.country_text_field).to_have(values.REGISTER_COUNTRY)

        with allure.step("Verify marketing messages agreement checkbox and toggle it"):
            expect(android_register.marketing_messages_agreement_check_box).to_be_checked()
            assert android_register.marketing_messages_agreement_check_box.click()
            expect(android_register.marketing_messages_agreement_check_box).not_.to_be_checked()

        with allure.step("Click on Create account button"):
            android_register.btn_create_account.click()

        with allure.step("Verify Learn Tab is loaded after completion"):
            expect(main_dashboard.learn_tab).to_be_displayed()
            expect(main_dashboard.learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)

        with allure.step("Goto Profile Tab and verify username and Full name"):
            assert main_dashboard.profile_tab.click()
            expect(profile_page.profile_username).to_have(f"@{username}")
            expect(profile_page.profile_txt_name).to_have(full_name)

        with allure.step("Delete account - Clean up"):
            assert main_dashboard.profile_tab.click()
            assert profile_page.settings_button.click()
            assert settings_page.settings_manage_account_text.click()
            assert profile_page.profile_settings_delete_account.click()
            assert profile_page.profile_settings_password_input.send_keys(password)
            assert profile_page.profile_settings_delete_account_confirm.click()
            assert android_landing.register_button.exists()
