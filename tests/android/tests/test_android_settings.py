"""
    Settings Screen Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.common.enums import ElementAttribute


class TestAndroidSettings:
    """
    Settings screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
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

        driver = android_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()

        profile_tab = main_dashboard_page.profile_tab
        expect(profile_tab).to_have(
            values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.CONTENT_DESC
        )
        expect(profile_tab).not_.to_be_selected()
        assert profile_tab.click()
        assert profile_page.settings_button.click()
        expect(profile_page.get_settings_screen_title).to_have(
            values.PROFILE_SETTINGS_UPPER_TEXT
        )
        manage_account_label = profile_page.get_manage_account_label
        expect(manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT_LABEL)

        video_label = profile_page.get_video_label
        expect(video_label).to_have(values.PROFILE_VIDEO_LABEL)

        assert profile_page.get_profile_txt_support_info.exists()
        assert profile_page.get_profile_txt_contact_support.exists()
        expect(profile_page.get_profile_txt_terms_of_use).to_have(
            values.PROFILE_TERMS_OF_USE_UPPERCASE
        )
        assert profile_page.privacy_policy_text.exists()
        profile_page.privacy_policy_text.scroll_vertically_from_element()
        expect(profile_page.get_profile_txt_cookie_policy).to_have(
            values.PROFILE_COOKIE_POLICY, case="lower"
        )
        expect(profile_page.get_profile_personal_info).to_have(
            values.PROFILE_PERSONAL_INFO
        )
        expect(profile_page.get_profile_txt_view_faq).to_have(values.PROFILE_FAQ)
        expect(profile_page.get_profile_personal_info).to_have(
            values.PROFILE_PERSONAL_INFO
        )
        expect(profile_page.get_profile_app_version_code).to_have(
            values.ANDROID_APP_VERSION
        )
        expect(profile_page.get_profile_txt_up_to_date).to_have(
            values.PROFILE_APP_UP_TO_DATE
        )
        assert profile_page.profile_txt_logout.exists()

    def test_load_profile_elements(self, android_login, setup_logging):
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

        driver = android_login
        profile_page = AndroidProfile()

        profile_page.get_profile_txt_contact_support.scroll_vertically_from_element()
        manage_account_label = profile_page.get_manage_account_label
        expect(manage_account_label).to_have(values.PROFILE_MANAGE_ACCOUNT_LABEL)
        assert manage_account_label.click()
        back_button = profile_page.back_navigation_button
        expect(back_button).to_be_displayed()
        assert back_button.click()

        video_label = profile_page.get_video_label
        expect(video_label).to_have(values.PROFILE_VIDEO_LABEL)
        assert video_label.click()
        back_button = profile_page.back_navigation_button
        expect(back_button).to_be_displayed()
        assert back_button.click()

        terms_of_use = profile_page.get_profile_txt_terms_of_use
        assert terms_of_use.click()
        expect(profile_page.text_toolbar_title).to_have(
            values.PROFILE_TERMS_OF_USE_UPPERCASE
        )
        assert profile_page.back_navigation_button.click()

        assert profile_page.privacy_policy_text.click()
        expect(profile_page.text_toolbar_title).to_have(
            values.PROFILE_PRIVACY_POLICY, case="lower"
        )
        assert profile_page.back_navigation_button.click()
        profile_page.privacy_policy_text.scroll_vertically_from_element()
        assert profile_page.get_profile_txt_cookie_policy.click()
        expect(profile_page.text_toolbar_title).to_have(
            values.PROFILE_COOKIE_POLICY, case="lower"
        )
        assert profile_page.back_navigation_button.click()

        assert profile_page.get_profile_personal_info.click()
        expect(profile_page.text_toolbar_title).to_have(values.PROFILE_PERSONAL_INFO)
        assert profile_page.back_navigation_button.click()
