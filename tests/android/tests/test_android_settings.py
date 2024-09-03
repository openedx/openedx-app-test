
"""
    Settings Screen Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidSettings:
    """
    Settings screen's Test Case
    """

    def test_start_settings_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidSettings.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_done_button().click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon, "Profile" as Title, Edit
                Profile Image, User Name, Video Settings
                Support Info, Contact Support, Terms of Use
                Privacy Policy, Cookie Policy, Personal Info
                View FAQ, App Version, Up to Date
                Logout button
        """

        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        profile_page = AndroidProfile(set_capabilities, setup_logging)
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

        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())
        assert profile_page.get_profile_txt_cookie_policy().text.lower() == values.PROFILE_COOKIE_POLICY
        assert profile_page.get_profile_personal_info().text == values.PROFILE_PERSONAL_INFO
        assert profile_page.get_profile_txt_view_faq().text == values.PROFILE_FAQ
        assert profile_page.get_profile_app_version_code().text == values.ANDROID_APP_VERSION
        assert profile_page.get_profile_txt_up_to_date().text == values.PROFILE_APP_UP_TO_DATE
        assert profile_page.get_profile_txt_logout().text.lower() == values.PROFILE_LOGOUT_BUTTON

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

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.scroll_screen(set_capabilities, profile_page.get_profile_txt_contact_support(),
                                       profile_page.get_profile_txt_view_faq())
        manage_account_label = profile_page.get_manage_account_label()
        assert manage_account_label.text == values.PROFILE_MANAGE_ACCOUNT_LABEL
        manage_account_label.click()
        back_button = global_contents.get_back_button(set_capabilities)
        assert back_button.get_attribute('displayed') == values.TRUE_LOWERCASE
        back_button.click()

        video_label = profile_page.get_video_label()
        assert video_label.text == values.PROFILE_VIDEO_LABEL
        video_label.click()
        back_button = global_contents.get_back_button(set_capabilities)
        assert back_button.get_attribute('displayed') == values.TRUE_LOWERCASE
        back_button.click()

        terms_of_use = profile_page.get_profile_txt_terms_of_use()
        terms_of_use.click()
        assert global_contents.get_txt_toolbar_title(set_capabilities).text == values.PROFILE_TERMS_OF_USE_UPPERCASE
        global_contents.get_back_button(set_capabilities).click()

        profile_page.get_profile_txt_privacy_policy().click()
        assert global_contents.get_txt_toolbar_title(set_capabilities).text.lower() == values.PROFILE_PRIVACY_POLICY
        global_contents.get_back_button(set_capabilities).click()

        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())
        profile_page.get_profile_txt_cookie_policy().click()
        assert global_contents.get_txt_toolbar_title(set_capabilities).text.lower() == values.PROFILE_COOKIE_POLICY
        global_contents.get_back_button(set_capabilities).click()

        profile_page.get_profile_personal_info().click()
        assert global_contents.get_txt_toolbar_title(set_capabilities).text == values.PROFILE_PERSONAL_INFO
        global_contents.get_back_button(set_capabilities).click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)

        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
