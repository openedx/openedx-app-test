"""
Settings Screen Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.conftest import ios_login
from tests.ios.pages.ios_profile import IosProfile
from tests.common import values
from tests.common.globals import Globals


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

        expect(ios_profile.navigation_bar_title).to_have(values.PROFILE_SCREEN_TITLE, ElementAttribute.NAME)
        assert ios_profile.profile_img_profile.exists()
        expect(ios_profile.profile_user_name_text).to_have(values.PROFILE_NAME_TEXT)
        expect(ios_profile.profile_user_username_text).to_have(values.PROFILE_USERNAME_TEXT)
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT)
        assert ios_profile.profile_settings_button.click()
        expect(ios_profile.get_profile_settings_text).to_have(values.PROFILE_SETTINGS_UPPER_TEXT)
        expect(ios_profile.get_profile_manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT)
        expect(ios_profile.get_profile_video_settings_button).to_have(values.PROFILE_VIDEO_SETTINGS)
        expect(ios_profile.get_profile_support_info_text).to_have(values.PROFILE_SUPPORT_INFO)
        expect(ios_profile.get_profile_tos_text).to_have(values.PROFILE_TERMS_OF_USE)
        expect(ios_profile.get_profile_privacy_policy).to_have(values.PROFILE_PRIVACY_POLICY, case='lower')
        expect(ios_profile.get_profile_cookies_policy).to_have(values.PROFILE_COOKIE_POLICY, case='lower')
        expect(ios_profile.get_profile_dont_sell_data).to_have(values.PROFILE_PERSONAL_INFO)
        expect(ios_profile.get_profile_contact_support).to_have(values.PROFILE_CONTACT_SUPPORT, case='lower')
        expect(ios_profile.get_profile_view_faq).to_have(values.PROFILE_FAQ)
        expect(ios_profile.get_profile_version_info).to_have(values.IOS_APP_VERSION)
        expect(ios_profile.get_profile_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON, case='lower')

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
        manage_account = ios_profile.get_profile_manage_account_label
        expect(manage_account).to_have(values.PROFILE_MANAGE_ACCOUNT)
        assert manage_account.click()
        assert ios_profile.get_profile_manage_account_label.exists()
        manage_account_title = ios_profile.get_manage_account_title
        expect(manage_account_title).to_have(values.PROFILE_MANAGE_ACCOUNT)
        assert ios_profile.back_navigation_button.click()
        expect(ios_profile.get_profile_manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT)

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

        terms_of_use = ios_profile.get_profile_tos_text
        expect(terms_of_use).to_have(values.PROFILE_TERMS_OF_USE)
        terms_of_use.scroll_vertically_from_element()
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
