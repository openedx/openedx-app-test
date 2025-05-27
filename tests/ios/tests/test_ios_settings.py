"""
Settings Screen Test Module
"""

import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute, ScrollDirections
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.common import values
from tests.common.globals import Globals


@pytest.mark.IOS
class TestIosSettings:
    """
    Settings screen's Test Case
    """

    def test_ui_elements_smoke(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon, "Profile" as Title, Edit
                Profile Image, Username, Video Settings
                Support Info, Contact Support, Terms of Use
                Privacy Policy, Cookie Policy, Personal Info
                View FAQ, App Version, Up to Date
                Logout button
        """
        Element.set_driver(ios_login)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()
        main_dashboard = IosMainDashboard()
        global_contents = Globals(setup_logging)

        main_dashboard.profile_tab.click()
        expect(ios_profile.navigation_bar_title).to_have(values.PROFILE_SCREEN_TITLE, ElementAttribute.NAME)
        expect(ios_profile.profile_img_profile).to_exist()
        expect(ios_profile.profile_user_name_text).to_have(values.PROFILE_NAME_TEXT, ElementAttribute.LABEL)
        expect(ios_profile.profile_user_username_text).to_have(values.PROFILE_USERNAME_TEXT, ElementAttribute.LABEL)
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT, ElementAttribute.LABEL)
        ios_profile.profile_settings_button.click()
        expect(ios_profile.get_profile_settings_text).to_have(
            values.PROFILE_SETTINGS_UPPER_TEXT, ElementAttribute.LABEL
        )
        expect(ios_profile.profile_manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT, ElementAttribute.LABEL)
        expect(ios_profile.get_profile_video_settings_button).to_have(
            values.PROFILE_VIDEO_SETTINGS, ElementAttribute.LABEL
        )
        expect(ios_profile.get_profile_support_info_text).to_have(values.PROFILE_SUPPORT_INFO, ElementAttribute.LABEL)
        Element.swipe_vertical_full_page()
        Element.swipe_vertical_full_page()
        expect(ios_profile.get_profile_tos_text).to_have(values.PROFILE_TERMS_OF_USE, ElementAttribute.LABEL)
        expect(ios_profile.get_profile_privacy_policy).to_have(
            values.PROFILE_PRIVACY_POLICY, ElementAttribute.LABEL, case="lower"
        )
        expect(ios_profile.get_profile_cookies_policy).to_have(
            values.PROFILE_COOKIE_POLICY, ElementAttribute.LABEL, case="lower"
        )
        expect(ios_profile.get_profile_dont_sell_data).to_have(values.PROFILE_PERSONAL_INFO, ElementAttribute.LABEL)
        expect(ios_profile.get_profile_contact_support).to_have(
            values.PROFILE_CONTACT_SUPPORT, ElementAttribute.LABEL, case="lower"
        )
        expect(ios_profile.get_profile_view_faq).to_have(values.PROFILE_FAQ, ElementAttribute.LABEL)
        ios_profile.verify_app_version(global_contents.app_version)
        expect(ios_profile.get_profile_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON_IOS, ElementAttribute.LABEL)

    def test_load_manage_account(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping manage account will load manage account screen
            Verify manage account screen is loaded successfully with its header contents
            Verify that tapping back button should leave manage account screen
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()
        Element.swipe_vertical_full_page(ScrollDirections.DOWN)
        if not ios_profile.profile_manage_account_label.exists(raise_exception=False):
            Element.swipe_vertical_full_page(ScrollDirections.DOWN)
        expect(ios_profile.profile_manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT, ElementAttribute.LABEL)
        ios_profile.profile_manage_account_label.click()
        expect(ios_profile.profile_manage_account_title).to_exist()
        expect(ios_profile.profile_manage_account_title).to_have(values.PROFILE_MANAGE_ACCOUNT, ElementAttribute.LABEL)
        ios_profile.back_navigation_button.click()
        expect(ios_profile.profile_manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT, ElementAttribute.LABEL)

    def test_load_video_settings(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping manage account will load manage account screen
            Verify manage account screen is loaded successfully with its header contents
            Verify that tapping back button should leave manage account screen
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()

        video_settings = ios_profile.get_profile_video_settings_button
        expect(video_settings).to_have(values.PROFILE_VIDEO_SETTINGS)
        assert video_settings.click()
        video_settings_title = ios_profile.get_manage_account_title
        expect(video_settings_title).to_have(values.PROFILE_VIDEO_SETTINGS)
        assert ios_profile.back_navigation_button.click()
        expect(ios_profile.get_profile_video_settings_button).to_have(values.PROFILE_VIDEO_SETTINGS)

    def test_load_profile_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping edit button should load Edit profile screen
            Verify that tapping back button should leave Edit profile screen
            Verify that tapping leave button should leave Edit profile screen
            Verify that tapping Video Settings should load Video Settings screen
            Verify that tapping back button should leave Video Settings screen
            Verify that tapping Terms of Use should load Terms of Use screen
            Verify that tapping back button should leave Terms of Use screen
            Verify that tapping Privacy Policy should load Privacy Policy screen
            Verify that tapping back button should leave Privacy Policy screen
            Verify that tapping Cookie Policy should load Cookie Policy screen
            Verify that tapping back button should leave Cookie Policy screen
            Verify that tapping Personal Info should load Personal Info screen
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()
        global_contents = Globals(setup_logging)

        Element.swipe_vertical_full_page()
        terms_of_use = ios_profile.get_profile_tos_text
        expect(terms_of_use).to_have(values.PROFILE_TERMS_OF_USE)
        assert terms_of_use.click()
        expect(ios_profile.screen_heading_title).to_have(values.PROFILE_TERMS_OF_USE)
        assert ios_profile.back_navigation_button.click()

        assert ios_profile.get_profile_privacy_policy.click()
        assert global_contents.get_screen_heading_title(set_capabilities).text.lower() == values.PROFILE_PRIVACY_POLICY
        assert ios_profile.back_navigation_button.click()

        assert ios_profile.get_profile_cookies_policy.click()
        assert global_contents.get_screen_heading_title(set_capabilities).text.lower() == values.PROFILE_COOKIE_POLICY
        assert ios_profile.back_navigation_button.click()

        assert ios_profile.get_profile_dont_sell_data.click()
        expect(ios_profile.screen_heading_title).to_have(values.PROFILE_PERSONAL_INFO)
        assert ios_profile.back_navigation_button.click()
