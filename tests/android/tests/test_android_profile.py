
"""
    Profile Screen Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.conftest import android_login


class TestAndroidProfile:
    """
    Profile screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon 
                "Profile" as Title
                Edit Profile Button
                Profile Image
                Username
                Video Settings
        """
        driver = android_login()
        main_dashboard_page = AndroidMainDashboard(driver, setup_logging)
        profile_page = AndroidProfile(driver, setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        assert profile_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        profile_tab.click()
        assert profile_page.get_settings_button().get_attribute('content-desc').lower() == values.PROFILE_SETTINGS_TEXT
        assert values.PROFILE_IMAGE_TEXT in profile_page.get_profile_img_profile().get_attribute('content-desc')
        assert profile_page.get_profile_txt_name().text == values.PROFILE_NAME_TEXT
        assert profile_page.get_profile_username().text == values.PROFILE_USERNAME_TEXT
        assert profile_page.get_edit_profile_button().text == values.EDIT_PROFILE_TITLE
