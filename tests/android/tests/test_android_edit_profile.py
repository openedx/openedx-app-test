
"""
    Edit Profile Screen Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_edit_profile import  AndroidEditProfile
from tests.common import values


class TestAndroidEditProfile:
    """
    Profile screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
        Scenarios:
            Verify that on clicking edit profile button,
            Edit Profile screen will show following contents:
            Verify that Edit Profile screen will show following contents:
                Back icon
                "Edit Profile" as Title
                Done button
                Profile type
                Limited profile message
                Profile Image
                Username
                Location label
                Location
                Spoken Language label
                Spoken Language
                About Me label
                About Me placeholder
        """

        driver = android_login
        main_dashboard_page = AndroidMainDashboard(driver, setup_logging)
        profile_page = AndroidProfile(driver, setup_logging)
        edit_profile_page = AndroidEditProfile(driver, setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        assert profile_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        profile_tab.click()
        assert profile_page.get_settings_button().get_attribute('content-desc').lower() == values.PROFILE_SETTINGS_TEXT
        assert values.PROFILE_NAME_TEXT in profile_page.get_profile_img_profile().get_attribute('content-desc')
        assert profile_page.get_profile_txt_name().text == values.PROFILE_NAME_TEXT
        assert profile_page.get_profile_username().text == values.PROFILE_USERNAME_TEXT
        assert profile_page.get_edit_profile_button().text == values.EDIT_PROFILE_TITLE
        profile_page.get_edit_profile_button().click()
        assert edit_profile_page.get_edit_profile_title().text == values.EDIT_PROFILE_TITLE
        assert edit_profile_page.get_done_button().text == values.EDIT_PROFILE_DONE_BUTTON
        assert edit_profile_page.get_back_button().get_attribute('displayed') == values.TRUE_LOWERCASE
        assert edit_profile_page.get_edit_profile_type_label().text == values.EDIT_PROFILE_TYPE_LABEL
        assert edit_profile_page.get_edit_profile_user_name().text == values.EDIT_PROFILE_USER_NAME
        assert edit_profile_page.get_edit_profile_limited_profile_message().text == values.EDIT_PROFILE_MESSAGE
        assert edit_profile_page.get_edit_profile_txt_label_location().text == values.EDIT_PROFILE_LOCATION_LABEL
        assert edit_profile_page.get_edit_profile_tf_select_location().text == values.EDIT_PROFILE_LOCATION
        assert edit_profile_page.get_edit_profile_txt_label_spoken_language().text == values.EDIT_PROFILE_LANGUAGE_LABEL
        assert edit_profile_page.get_edit_profile_select_spoken_language().text == values.EDIT_PROFILE_LANGUAGE
        assert edit_profile_page.get_edit_profile_txt_label_about_me().text == values.EDIT_PROFILE_ABOUT_ME_LABEL
        assert edit_profile_page.get_edit_profile_txt_placeholder_about_me().text == values.EDIT_PROFILE_ABOUT_ME
