"""Test iOS Regression Settings Screen"""

import allure
import pytest
from framework import expect
from framework.element import Element
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_settings_page import IosSettings


@allure.suite("iOS")
@allure.feature("Settings")
@allure.story("Settings Screen")
@pytest.mark.IOS_REGRESSION
class TestIosRegressionSettingsScreen:
    """
    Settings screen's Test Case
    """

    def test_ios_regression_settings_screen(self, ios_login, setup_logging):
        """
        test ios regression settings screen
        Scenarios:
            1 Goto Profile
            2 Click on settings icon
                verify screen title “Settings”
                verify back arrow button
                verify button text “Manage Account”
            3 Click on Manage Account button
                verify screen title “Manage Account”
                verify username and user-email
                verify Edit Profile button is clickable/enabled
                verify Edit profile button text
                verify Delete Account button is clickable/enabled
                verify Delete Account button text
            4 Click on Delete Account button
                verify screen title “Delete Account”
                verify waring message “Are you sure you want to delete your account?”
                verify msg “To confirm this action, please enter your account password”
                verify Password field title
                verify password field is active
                verify Back to profile button exists
                verify Yes, delete account text exists and button is inactive
            5 Enter any password
                verify delete account button is active
            6 click on back to profile button
                verify Manage account screen is opened
            7 Click on back arrow button
                verify screen title “Settings”
                verify category heading “Settings”
                verify button text “Video”
            8 Click on Video
                verify screen title “Video”
                verify back arrow button
                verify options  with sub texts
                Wi-fi only download (“Only download content when wi-fi is turned on”)
                Video streaming quality (“Auto”)
                Video download quality (“Auto”)
                verify wi-fi only download has toggle button
            9 Click on wifi only download toggle button
                toggle is turned off
            10 Click on wifi only download toggle button
                toggle is turned on
            11 Click on Video streaming quality
                verify screen title “Video streaming quality”
                verify following options are shown
                    Auto (Recommended)
                    360p (Lower data usage)
                    540p
                    720p (Best quality)
            12 Click on 360p
                verify check mark against 360p option
            13 click on back arrow
                verify values under Video streaming quality is updated to 360p
            14 Click on Video streaming quality
            15 Click on Auto
                verify check mark against Auto option
            16 click on back arrow
                verify values under Video streaming quality is updated to Auto

            Click on Video download quality
                verify screen title “Video download quality”
                verify following options are shown
                    Auto (Recommended)
                    360p (Lower data usage)
                    540p
                    720p (Best quality)

            Click on 360p
                verify check mark against 360p option
            click on back arrow
                verify values under Video download quality is updated to 360p
            Click on Video download quality

            Click on Auto
                verify check mark against Auto option
            click on back arrow
                verify values under Video download quality is updated to Auto

            Click on back arrow button
                verify category heading “Purchases”
            17 Click on “Restore Purchases”
                verify purchases restored dialogue message
                verify Get help button exists
                verify Cancel button exists
                verify category heading “Support”
            18 Click on Help us Improve
                verify google form is loaded
            19 Click on Contact Support
                verification not be possible
                verify email template is loaded in default email app
            20 Click on Terms of Use
                verify “Terms of Use”
                verify title “edX Terms of Service”
            21 click on back arrow
            22 click on Privacy Policy
                verify “Privacy Policy”
                verify title “edX Privacy Policy”
            23 click on back arrow
            24 click on Cookie Policy
                verify “Cookie Policy”
                verify title “edX’s Cookie Policy”
            25 Click Do not sell my personal information
                verify screen title “Do not sell my personal information”
                verify title “Manage Consent Preferences”
                verify toggle text “Share My Information with Third Parties for Personalized Advertising”
                verify toggle is turned on
            26 click on toggle
                verify toggle is turned off
            27 click on toggle
                verify toggle is turned on
            28 click on back arrow
            29 click on view FAQ
                support page is loaded in browser
            30 Go back to settings screen
                verify app version is displayed
                verify text “Up-to-date” with check mark
                verify log out button and icon appears
            31 Click on Log out button
                verify landing page is load and sign in button is visible
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        ios_settings = IosSettings()
        main_dashboard = IosMainDashboard()
        ios_profile = IosProfile()
        global_contents = Globals(setup_logging)

        with allure.step("Goto Profile"):
            main_dashboard.profile_tab.click()

        with allure.step("Click on settings icon"):
            ios_profile.profile_settings_button.click()
            expect(ios_settings.screen_title).to_have(values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL)
            expect(ios_settings.back_navigation_button).to_exist()
            expect(ios_settings.manage_account_button).to_exist()

        with allure.step("Click on Manage Account button"):
            ios_settings.manage_account_button.click()
            expect(ios_settings.manage_account_screen_title).to_have(
                values.PROFILE_MANAGE_ACCOUNT_LABEL, ElementAttribute.LABEL
            )
            expect(ios_settings.manage_account_username).to_have(values.PROFILE_NAME_TEXT, ElementAttribute.LABEL)
            expect(ios_settings.manage_account_useremail).to_have(values.AUTOMATION_USER_EMAIL, ElementAttribute.LABEL)
            expect(ios_settings.manage_account_edit_profile_button).to_be_enabled()
            expect(ios_settings.manage_account_edit_profile_button).to_have(
                values.EDIT_PROFILE_TITLE, ElementAttribute.LABEL
            )
            expect(ios_settings.manage_account_delete_account_button).to_be_enabled()
            expect(ios_settings.manage_account_delete_account_button).to_have(
                values.PROFILE_DELETE_ACCOUNT_TEXT, ElementAttribute.LABEL
            )

        with allure.step("Click on Delete Account button"):
            ios_settings.manage_account_delete_account_button.click()
            expect(ios_settings.navigation_bar_title).to_have(values.PROFILE_DELETE_ACCOUNT_TEXT, ElementAttribute.NAME)
            expect(ios_settings.are_you_sure_text).to_have(
                values.DELETE_ACCOUNT_WARNING_MESSAGE, ElementAttribute.LABEL
            )
            expect(ios_settings.delete_account_desc_text).to_have(
                values.DELETE_ACCOUNT_DESCRIPTION, ElementAttribute.LABEL
            )
            expect(ios_settings.password_filed_title).to_have(values.PASSWORD, ElementAttribute.LABEL)
            expect(ios_settings.password_textfield).to_be_enabled()
            expect(ios_settings.yes_delete_account).not_.to_be_enabled()
            expect(ios_settings.back_arrow_button).to_exist()
            expect(ios_settings.back_to_profile_button).to_have(values.BACK_TO_PROFILE_BUTTON, ElementAttribute.LABEL)

        with allure.step("Enter any password"):
            expect(ios_settings.password_filed_title).to_have(values.PASSWORD, ElementAttribute.LABEL)
            ios_settings.password_textfield.send_keys("random_string" + "\n")
            expect(ios_settings.yes_delete_account).to_be_enabled()

        with allure.step("click on back to manage account screen"):
            ios_settings.back_to_profile_button.click()
            expect(ios_settings.manage_account_screen_title).to_have(
                values.PROFILE_MANAGE_ACCOUNT_LABEL, ElementAttribute.LABEL
            )
            ios_settings.manage_account_delete_account_button.click()
            ios_settings.delete_account_screen_back_navigation_button.click()
            expect(ios_settings.manage_account_screen_title).to_have(
                values.PROFILE_MANAGE_ACCOUNT_LABEL, ElementAttribute.LABEL
            )

        with allure.step("Click on back arrow button"):
            ios_settings.back_navigation_button.click()
            expect(ios_settings.screen_title).to_have(values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL)
            expect(ios_settings.settings_category_text).to_have(
                values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL
            )
            expect(ios_settings.video_settings_button).to_exist()

        with allure.step("Click on Video"):
            ios_settings.video_settings_button.click()
            expect(ios_settings.video_settings_screen_title).to_have(
                values.PROFILE_VIDEO_SETTINGS, ElementAttribute.LABEL
            )
            expect(ios_settings.back_navigation_button).to_exist()
            expect(ios_settings.find_by_text_on_screen(values.WIFI_ONLY_DOWNLOAD_LABEL)).to_exist()
            expect(ios_settings.find_by_text_on_screen(values.WIFI_ONLY_DOWNLOAD_SUB_TEXT)).to_exist()
            expect(ios_settings.download_agreement_switch).to_have(
                values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE
            )
            expect(ios_settings.video_download_quality_button).to_have(
                values.VIDEO_DOWNLOAD_QUALITY_BUTTON_LABEL, ElementAttribute.LABEL
            )
            expect(ios_settings.video_stream_quality_button).to_have(
                values.VIDEO_STREAM_QUALITY_BUTTON_LABEL, ElementAttribute.LABEL
            )
            expect(ios_settings.video_stream_quality_arrow_icon).to_be_enabled()
            expect(ios_settings.video_download_quality_arrow_icon).to_be_enabled()

        with allure.step("Click on wifi only download toggle button"):
            ios_settings.download_agreement_switch.click()
            expect(ios_settings.download_agreement_switch).to_have(
                values.IOS_UNSELECTED_TAB_VALUE, ElementAttribute.VALUE
            )

        with allure.step("Click on wifi only download toggle button again"):
            ios_settings.download_agreement_switch.click()
            expect(ios_settings.download_agreement_switch).to_have(
                values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE
            )

        with allure.step("Click on Video streaming quality"):
            ios_settings.video_stream_quality_button.click()
            expect(ios_settings.find_by_text_on_screen(values.HEADING_VIDEO_STREAMING_QUALITY)).to_exist()
            expect(ios_settings.quality_option_auto).to_contain(values.AUTO_QUALITY, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_auto).to_contain(values.RECOMMENDED_TEXT, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_360p).to_contain(values.QUALITY_360P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_360p).to_contain(values.LOWER_DATA_USAGE, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_540p).to_contain(values.QUALITY_540P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_720p).to_contain(values.QUALITY_720P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_720p).to_contain(values.BEST_QUALITY, ElementAttribute.LABEL)
            ios_settings.back_navigation_button.click()

        with allure.step("Click on Video download quality"):
            ios_settings.video_download_quality_button.click()
            expect(ios_settings.find_by_text_on_screen(values.HEADING_VIDEO_DOWNLOAD_QUALITY)).to_exist()
            expect(ios_settings.quality_option_auto).to_contain(values.AUTO_QUALITY, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_auto).to_contain(values.RECOMMENDED_TEXT, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_360p).to_contain(values.QUALITY_360P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_360p).to_contain(values.LOWER_DATA_USAGE, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_540p).to_contain(values.QUALITY_540P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_720p).to_contain(values.QUALITY_720P, ElementAttribute.LABEL)
            expect(ios_settings.quality_option_720p).to_contain(values.BEST_QUALITY, ElementAttribute.LABEL)

        with allure.step("Click on back arrow button"):
            ios_settings.back_navigation_button.click()
            ios_settings.back_navigation_button.click()
            expect(ios_settings._purchase_category_text).to_have(values.HEADING_PURCHASES, ElementAttribute.LABEL)
            expect(ios_settings.restore_purchase_title).to_have(values.HEADING_PURCHASES_TITLE, ElementAttribute.LABEL)
            expect(ios_settings.restore_message_text).to_have(values.HEADING_PURCHASES_MSG, ElementAttribute.LABEL)
            expect(ios_settings.restore_purchase_button).to_exist()

        with allure.step("Click on Restore Purchases"):
            ios_settings.restore_purchase_button.click()
            expect(ios_settings.restore_purchase_dialogue_title).to_have(
                values.PURCHASES_RESTORED_MESSAGE, ElementAttribute.LABEL
            )
            expect(ios_settings.restore_purchase_get_help_button).to_have(
                values.RESTORE_PURSCHASE_GET_HELP_BUTTON_LABEL, ElementAttribute.LABEL
            )
            expect(ios_settings.restore_purchase_cancel_button).to_have(
                values.RESTORE_PURSCHASE_CLOSE_BUTTON_LABEL, ElementAttribute.LABEL
            )
            expect(ios_settings.find_by_text_on_screen(values.RESTORE_PURSCHASE_DESCRIPTION)).to_exist()

        with allure.step("Click on close button"):
            ios_settings.restore_purchase_cancel_button.click()
            expect(ios_settings.restore_purchase_dialogue_title).not_.to_exist()
            expect(ios_settings.support_info_category_text).to_have(values.PROFILE_SUPPORT_INFO, ElementAttribute.LABEL)

        with allure.step("verify support options"):
            expect(ios_settings.help_us_improve_button).to_have(values.SUPPORT_HELP_US_IMPROVE, ElementAttribute.LABEL)
            expect(ios_settings.contact_support_button).to_have(values.PROFILE_CONTACT_SUPPORT, ElementAttribute.LABEL)
            expect(ios_settings.terms_of_use_button).to_have(values.PROFILE_TERMS_OF_USE, ElementAttribute.LABEL)
            Element.swipe_vertical_full_page()
            expect(ios_settings.privacy_policy_button).to_have(values.PROFILE_PRIVACY_POLICY, ElementAttribute.LABEL)
            expect(ios_settings.cookie_policy_button).to_have(values.PROFILE_COOKIE_POLICY, ElementAttribute.LABEL)
            expect(ios_settings.donot_sell_my_info_button).to_have(values.PROFILE_PERSONAL_INFO, ElementAttribute.LABEL)
            expect(ios_settings.view_faq_button).to_have(values.PROFILE_FAQ, ElementAttribute.LABEL)

        with allure.step("Click on Terms of Use"):
            ios_settings.terms_of_use_button.click()
            expect(ios_settings.accept_cookies_button).to_exist()
            expect(ios_settings.reject_cookies_button).to_exist()
            expect(ios_settings.privacy_choices_button).to_exist()
            ios_settings.accept_cookies_button.click()
            expect(ios_settings.screen_heading_title).to_have(values.PROFILE_TERMS_OF_USE, ElementAttribute.LABEL)
            expect(ios_settings.edx_terms_of_use_heading_text).to_have(
                values.EDX_TERMS_OF_SERVICE_HEADING_TEXT, ElementAttribute.LABEL
            )
            ios_settings.back_navigation_button.click()

        with allure.step("Click on Privacy Policy"):
            ios_settings.privacy_policy_button.click()
            expect(ios_settings.screen_heading_title).to_have(values.PROFILE_PRIVACY_POLICY, ElementAttribute.LABEL)
            expect(ios_settings.edx_privacy_policy_heading_text).to_have(
                values.EDX_PRIVACY_POLICY_HEADING_TEXT, ElementAttribute.LABEL
            )
            ios_settings.back_navigation_button.click()

        with allure.step("Click on Cookie Policy"):
            ios_settings.cookie_policy_button.click()
            expect(ios_settings.screen_heading_title).to_have(values.PROFILE_COOKIE_POLICY, ElementAttribute.LABEL)
            expect(ios_settings.edx_cookie_policy_heading_text).to_have(
                values.EDX_COOKIE_POLICY_HEADING_TEXT, ElementAttribute.LABEL
            )
            ios_settings.back_navigation_button.click()

        with allure.step("Click Do not sell my personal information"):
            pass
            # TODO: Implement this step when the feature is fixed

        with allure.step("Click on view FAQ"):
            ios_settings.view_faq_button.click()
            expect(ios_settings.find_by_text_on_screen(values.EDX_LEARNER_HELP_CENTER)).to_exist()
            expect(ios_settings.learner_help_center_search_bar).to_exist()
            Element.switch_back_to_app()

        with allure.step("Verify app version and log out button"):
            ios_settings.verify_app_version(global_contents.app_version)
            expect(ios_profile.profile_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON_IOS, ElementAttribute.LABEL)
            expect(ios_settings.logout_arrow_icon).to_be_visible()
