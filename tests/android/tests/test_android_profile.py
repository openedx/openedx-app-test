
"""
    Profile Screen Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidProfile:
    """
    Profile screen's Test Case
    """

    def test_start_profile_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidProfile.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            # assert whats_new_page.navigate_features().text == 'Done'
            # whats_new_page.get_done_button().click()
            whats_new_page.get_close_button().click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon
                "Profile" as Title
                Edit
                Profile Image
                User Name
            Verify that Profile screen will show following contents for limited profile:
                Age limit text
                Account settings Button
            Verify that Profile screen will show following contents for Full profile:
                location
                Language (if selected)
                User Bio
        """

        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        profile_page = AndroidProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        assert profile_page.get_profile_screen_title().text == values.PROFILE_SCREEN_TITLE
        assert profile_page.get_profile_edit_button().text == values.PROFILE_EDIT_BUTTON
        assert profile_page.get_profile_img_profile().get_attribute('content-desc') == values.PROFILE_IMAGE_TEXT
        assert profile_page.get_profile_txt_name().text == values.PROFILE_NAME_TEXT
        assert profile_page.get_profile_username().text == values.PROFILE_USERNAME_TEXT
        assert profile_page.get_profile_txt_settings().text == values.PROFILE_SETTINGS_TEXT
        assert profile_page.get_profile_txt_video_settings().text == values.PROFILE_VIDEO_SETTINGS
        assert profile_page.get_profile_txt_support_info().text == values.PROFILE_SUPPORT_INFO
        assert profile_page.get_profile_txt_contact_support().text == values.PROFILE_CONTACT_SUPPORT
        assert profile_page.get_profile_txt_terms_of_use().text == values.PROFILE_TERMS_OF_USE
        assert profile_page.get_profile_txt_privacy_policy().text == values.PROFILE_PRIVACY_POLICY

        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())
        assert profile_page.get_profile_txt_cookie_policy().text == values.PROFILE_COOKIE_POLICY
        assert profile_page.get_profile_personal_info().text == values.PROFILE_PERSONAL_INFO
        assert profile_page.get_profile_txt_view_faq().text == values.PROFILE_FAQ
        assert profile_page.get_profile_app_version_code().text == values.ANDROID_APP_VERSION
        assert profile_page.get_profile_txt_up_to_date().text == values.PROFILE_APP_UP_TO_DATE
        assert profile_page.get_profile_txt_logout().text == values.PROFILE_LOGOUT_BUTTON

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from main dashboard screen
        """

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)

        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_close_button()
        assert profile_page.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        profile_page.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
