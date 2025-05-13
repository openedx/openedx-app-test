"""Android - Regression - settings screen"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_settings_page import AndroidSettingsPage
from tests.android.pages.manage_account_page import ManageAccountPage
from tests.common import values
from tests.common.globals import Globals


@allure.epic("Accounts")
@allure.feature("Sign In")
@allure.story("edit profile")
@pytest.mark.ANDROID_REGRESSION
class TestRegressionSettingsScreen:
    """Test profile edit functionality"""

    def test_regression_settings_screen(self, android_login, setup_logging):
        """
        Test Regression Settings Screen
        """
        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        profile_page = AndroidProfile()
        main_dashboard_page = AndroidMainDashboard()
        manage_account_page = ManageAccountPage()
        edit_profile_page = AndroidEditProfile()
        settings_page = AndroidSettingsPage()
        global_contents = Globals(setup_logging)

        with allure.step("Goto Profile Tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("Click on settings icon"):
            profile_page.settings_button.click()
            expect(settings_page.title_text_settings).to_exist()
            expect(profile_page.profile_settings_back_button).to_exist()
            expect(settings_page.settings_manage_account_text).to_exist()

        with allure.step("Click on Manage Account button"):
            settings_page.settings_manage_account_text.click()
            expect(manage_account_page.text_toolbar_title).to_have(values.PROFILE_MANAGE_ACCOUNT)
            expect(manage_account_page.profile_name_text).to_have(values.PROFILE_NAME_TEXT)
            expect(manage_account_page.profile_username).to_have(values.PROFILE_USER_EMAIL_TEXT)

        with allure.step("verify Edit Profile button is clickable/enabled"):
            expect(manage_account_page.edit_profile_button).to_be_enabled()
            expect(manage_account_page.edit_profile_button).to_be_clickable()
            expect(manage_account_page.edit_profile_button_text).to_have(values.EDIT_PROFILE_TITLE)

        with allure.step("verify Delete Account button is clickable/enabled"):
            expect(manage_account_page.delete_account_button).to_be_clickable()
            expect(manage_account_page.delete_account_button).to_be_enabled()
            expect(manage_account_page.delete_account_button_text).to_have(values.PROFILE_DELETE_ACCOUNT_TEXT)
            expect(manage_account_page.delete_account_icon).to_exist()

        with allure.step("Click on Delete Account button"):
            profile_page.profile_settings_delete_account.click()
            expect(manage_account_page.delete_account_screen_title).to_have(values.PROFILE_DELETE_ACCOUNT_TITLE)
            expect(manage_account_page.delete_account_screen_warning_title).to_have(
                values.DELETE_ACCOUNT_WARNING_MESSAGE
            )
            expect(manage_account_page.delete_account_screen_description).to_have(values.DELETE_ACCOUNT_DESCRIPTION)
            expect(manage_account_page.password_label).to_have(values.PASSWORD)
            expect(manage_account_page.password_input_field).to_be_enabled()
            expect(manage_account_page.password_input_field).to_be_clickable()
            expect(manage_account_page.back_navigation_button).to_exist()
            expect(manage_account_page.yes_delete_account_button).not_.to_be_enabled()

        with allure.step("Enter any password"):
            manage_account_page.password_input_field.send_keys(values.PASSWORD)
            expect(manage_account_page.yes_delete_account_button).to_be_enabled()

        with allure.step("click on back button"):
            manage_account_page.back_navigation_button.click()
            expect(manage_account_page.text_toolbar_title).to_have(values.PROFILE_MANAGE_ACCOUNT)

        with allure.step("Click on Edit Profile button"):
            manage_account_page.edit_profile_button.click()
            expect(edit_profile_page.edit_profile_title).to_have(values.EDIT_PROFILE_TITLE)
            expect(edit_profile_page.edit_profile_user_name).to_have(values.EDIT_PROFILE_USER_NAME)

        with allure.step("Click on back button"):
            edit_profile_page.back_navigation_button.click()
            expect(manage_account_page.text_toolbar_title).to_have(values.PROFILE_MANAGE_ACCOUNT)
            manage_account_page.back_navigation_button.click()
            expect(settings_page.title_text_settings).to_exist()
            expect(settings_page.settings_category_text).to_exist()
            expect(settings_page.video_button_text).to_exist()

        with allure.step("Click on video button"):
            settings_page.video_button_text.click()
            expect(settings_page.text_toolbar_title).to_have(values.PROFILE_VIDEO_LABEL)
            expect(settings_page.back_navigation_button).to_exist()

        with allure.step("verify options  with sub texts"):
            expect(settings_page.wifi_only_label).to_have(values.WIFI_ONLY_DOWNLOAD_LABEL)
            expect(settings_page.wifi_only_description_label).to_have(values.WIFI_ONLY_DOWNLOAD_SUB_TEXT)
            settings_page.verify_video_download_quality_sub_text(values.AUTO)
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_DOWNLOAD_QUALITY)
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_STREAMING_QUALITY)
            AndroidSettingsPage.verify_video_streaming_quality_sub_text(values.AUTO)
            expect(settings_page.wifi_only_toggle_button).to_exist()

        with allure.step("Click on wifi only download toggle button"):
            settings_page.wifi_only_toggle_button.click()
            expect(settings_page.wifi_only_toggle_button).not_.to_be_checked()

        with allure.step("Click on wifi only download toggle button"):
            settings_page.wifi_only_toggle_button.click()
            expect(settings_page.wifi_only_toggle_button).to_be_checked()

        with allure.step("Click on Video streaming quality"):
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_STREAMING_QUALITY).click()
            expect(settings_page.text_toolbar_title).to_have(values.HEADING_VIDEO_STREAMING_QUALITY)
            settings_page.verify_all_video_quality_option_button_exist()
            settings_page.verify_all_video_quality_option_titles()
            settings_page.verify_all_video_quality_option_descriptions()
            settings_page.verify_video_quality_button_is_selected(values.AUTO)

        with allure.step("Click on 360p"):
            settings_page.get_video_quality_button(values.LOWEST_QUALITY).click()
            settings_page.verify_video_quality_button_is_selected(values.LOWEST_QUALITY)

        with allure.step("Click on back button"):
            settings_page.back_navigation_button.click()
            AndroidSettingsPage.verify_video_streaming_quality_sub_text(values.LOWEST_QUALITY)

        with allure.step("Click on Video streaming quality"):
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_STREAMING_QUALITY).click()

        with allure.step("Click on Auto"):
            settings_page.get_video_quality_button(values.AUTO).click()
            settings_page.verify_video_quality_button_is_selected(values.AUTO)

        with allure.step("Click on back button"):
            settings_page.back_navigation_button.click()
            AndroidSettingsPage.verify_video_streaming_quality_sub_text(values.AUTO)

        with allure.step("Click on Video download quality"):
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_DOWNLOAD_QUALITY).click()
            expect(settings_page.text_toolbar_title).to_have(values.HEADING_VIDEO_DOWNLOAD_QUALITY)
            settings_page.verify_all_video_quality_option_button_exist()
            settings_page.verify_all_video_quality_option_titles()
            settings_page.verify_all_video_quality_option_descriptions()
            settings_page.verify_video_quality_button_is_selected(values.AUTO)

        with allure.step("Click on 540p"):
            settings_page.get_video_quality_button(values.MEDIUM_QUALITY).click()
            settings_page.verify_video_quality_button_is_selected(values.MEDIUM_QUALITY)

        with allure.step("Click on back button"):
            settings_page.back_navigation_button.click()
            settings_page.verify_video_download_quality_sub_text(values.MEDIUM_QUALITY)

        with allure.step("Click on Video download quality"):
            settings_page.find_by_text_on_screen(values.HEADING_VIDEO_DOWNLOAD_QUALITY).click()

        with allure.step("Click on Auto"):
            settings_page.get_video_quality_button(values.AUTO).click()
            settings_page.verify_video_quality_button_is_selected(values.AUTO)

        with allure.step("Click on back button"):
            settings_page.back_navigation_button.click()
            settings_page.verify_video_download_quality_sub_text(values.AUTO)

        with allure.step("Click on back button"):
            settings_page.back_navigation_button.click()
            settings_page.find_by_text_on_screen(values.HEADING_PURCHASES)

        with allure.step("Click on “Restore Purchases”"):
            settings_page.restore_purchases_button_text.click()
            settings_page.android_loading_circle.exists(timeout=30)
            settings_page.android_loading_circle.wait_to_disappear()
            settings_page.find_by_text_on_screen(values.PURCHASES_RESTORED_MESSAGE)
            settings_page.find_by_text_on_screen(values.PURCHASES_RESTORED_DIALOGUE_CANCEL_TEXT)
            settings_page.find_by_text_on_screen(values.PURCHASES_RESTORED_DIALOGUE_GET_HELP_TEXT)
            settings_page.find_by_text_on_screen(values.PURCHASES_RESTORED_DIALOGUE_CANCEL_TEXT).click()

        with allure.step("Click on Help us Improve"):
            settings_page.help_us_improve_link.click()
            if settings_page.chrome_sign_in_dismiss_button.exists(20, False):
                settings_page.chrome_sign_in_dismiss_button.click(timeout=20)
            if settings_page.chrome_notifications_dismiss_button.exists(timeout=20, raise_exception=False):
                settings_page.chrome_notifications_dismiss_button.click(timeout=20)
            expect(settings_page.edx_feedback_google_form_title, timeout=20).to_exist()
            Element.switch_back_to_app()

        with allure.step("verify contact support element"):
            settings_page.find_by_text_on_screen(values.PROFILE_CONTACT_SUPPORT_ANDROID)
            Element.swipe_vertical_full_page()

        with allure.step("Click on terms of use"):
            settings_page.find_by_text_on_screen(values.PROFILE_TERMS_OF_USE_UPPERCASE).click()
            expect(settings_page.text_toolbar_title).to_have(values.PROFILE_TERMS_OF_USE_UPPERCASE)
            settings_page.find_by_text_on_screen("edX Terms of Service")
            settings_page.back_navigation_button.click()

        with allure.step("Click on privacy policy"):
            settings_page.find_by_text_on_screen(values.PROFILE_PRIVACY_POLICY_TITLE_CASE).click()
            expect(settings_page.text_toolbar_title).to_have(values.PROFILE_PRIVACY_POLICY_TITLE_CASE)
            settings_page.find_by_text_on_screen("edX Privacy Policy")
            settings_page.back_navigation_button.click()

        with allure.step("Click on cookie policy"):
            settings_page.find_by_text_on_screen(values.PROFILE_COOKIE_POLICY_TITLE_CASE).click()
            expect(settings_page.text_toolbar_title).to_have(values.PROFILE_COOKIE_POLICY_TITLE_CASE)
            settings_page.find_by_text_on_screen("edX’s Cookie Policy")
            settings_page.back_navigation_button.click()

        with allure.step("Click on personal info"):
            settings_page.find_by_text_on_screen(values.PROFILE_PERSONAL_INFO).click()
            expect(settings_page.text_toolbar_title).to_have(values.PROFILE_PERSONAL_INFO)
            expect(settings_page.share_my_info_button).to_exist()
            settings_page.back_navigation_button.click()

        with allure.step("click on View FAQ"):
            settings_page.find_by_text_on_screen(values.PROFILE_FAQ).click()
            settings_page.find_by_text_on_screen("edX Learner Help Center")
            settings_page.find_by_text_on_screen("Search for your answer below")
            Element.switch_back_to_app()

        with allure.step("verify app version and up-to-date text"):
            settings_page.verify_app_version(global_contents.app_version)
