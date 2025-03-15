"""
Profile Screen Test Module
"""

from tests.common import values
from tests.ios.pages.ios_profile import IosProfile
from tests.common.globals import Globals


class TestIosProfile:
    """
    Profile screen's Test Case
    """

    def test_ui_elements_smoke(self, ios_login, setup_logging):
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
        driver = ios_login
        ios_profile = IosProfile(driver, setup_logging)
        global_contents = Globals(setup_logging)

        assert global_contents.get_navigation_bar_title(driver)[0].get_attribute("name") == values.PROFILE_SCREEN_TITLE
        assert ios_profile.get_profile_img_profile()
        assert ios_profile.get_profile_user_name_text().text == values.PROFILE_NAME_TEXT
        assert ios_profile.profile_user_username_text().text == values.PROFILE_USERNAME_TEXT
        assert ios_profile.get_profile_settings_button().text == values.PROFILE_SETTINGS_TEXT
        assert (
            global_contents.get_element_by_name_ios(driver, values.EDIT_PROFILE_TITLE).text == values.EDIT_PROFILE_TITLE
        )
