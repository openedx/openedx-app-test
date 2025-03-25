
"""
    Settings Screen Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.common.globals import Globals


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
        main_dashboard_page = AndroidMainDashboard(driver, setup_logging)
        profile_page = AndroidProfile(driver, setup_logging)
        global_contents = Globals(setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        assert profile_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        profile_tab.click()
        profile_page.get_settings_button().click()

        assert profile_page.get_settings_screen_title().text == values.PROFILE_SETTINGS_UPPER_TEXT
        manage_account_label = profile_page.get_manage_account_label()
        assert manage_account_label.text == values.PROFILE_MANAGE_ACCOUNT_LABEL

        video_label = profile_page.get_video_label()
        assert video_label.text == values.PROFILE_VIDEO_LABEL
        assert profile_page.get_profile_txt_support_info().text == values.PROFILE_SUPPORT
        assert profile_page.get_profile_txt_contact_support().text.lower() == values.PROFILE_CONTACT_SUPPORT
        assert profile_page.get_profile_txt_terms_of_use().text == values.PROFILE_TERMS_OF_USE_UPPERCASE
        assert profile_page.get_profile_txt_privacy_policy().text.lower() == values.PROFILE_PRIVACY_POLICY

        global_contents.scroll_from_element(driver, profile_page.get_profile_txt_privacy_policy())
        assert profile_page.get_profile_txt_cookie_policy().text.lower() == values.PROFILE_COOKIE_POLICY
        assert profile_page.get_profile_personal_info().text == values.PROFILE_PERSONAL_INFO
        assert profile_page.get_profile_txt_view_faq().text == values.PROFILE_FAQ
        assert profile_page.get_profile_app_version_code().text == values.ANDROID_APP_VERSION
        assert profile_page.get_profile_txt_up_to_date().text == values.PROFILE_APP_UP_TO_DATE
        assert profile_page.get_profile_txt_logout().text.lower() == values.PROFILE_LOGOUT_BUTTON

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
        profile_page = AndroidProfile(driver, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.scroll_screen(driver, profile_page.get_profile_txt_contact_support(),
                                       profile_page.get_profile_txt_view_faq())
        manage_account_label = profile_page.get_manage_account_label()
        assert manage_account_label.text == values.PROFILE_MANAGE_ACCOUNT_LABEL
        manage_account_label.click()
        back_button = global_contents.get_back_button(driver)
        assert back_button.get_attribute('displayed') == values.TRUE_LOWERCASE
        back_button.click()

        video_label = profile_page.get_video_label()
        assert video_label.text == values.PROFILE_VIDEO_LABEL
        video_label.click()
        back_button = global_contents.get_back_button(driver)
        assert back_button.get_attribute('displayed') == values.TRUE_LOWERCASE
        back_button.click()

        terms_of_use = profile_page.get_profile_txt_terms_of_use()
        terms_of_use.click()
        assert global_contents.get_txt_toolbar_title(driver).text == values.PROFILE_TERMS_OF_USE_UPPERCASE
        global_contents.get_back_button(driver).click()

        profile_page.get_profile_txt_privacy_policy().click()
        assert global_contents.get_txt_toolbar_title(driver).text.lower() == values.PROFILE_PRIVACY_POLICY
        global_contents.get_back_button(driver).click()

        global_contents.scroll_from_element(driver, profile_page.get_profile_txt_privacy_policy())
        profile_page.get_profile_txt_cookie_policy().click()
        assert global_contents.get_txt_toolbar_title(driver).text.lower() == values.PROFILE_COOKIE_POLICY
        global_contents.get_back_button(driver).click()

        profile_page.get_profile_personal_info().click()
        assert global_contents.get_txt_toolbar_title(driver).text == values.PROFILE_PERSONAL_INFO
        global_contents.get_back_button(driver).click()
