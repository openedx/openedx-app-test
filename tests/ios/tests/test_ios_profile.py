"""
Profile Screen Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.common import values
from tests.ios.pages.ios_profile import IosProfile


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
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()
        expect(ios_profile.navigation_bar_title).to_have(values.PROFILE_SCREEN_TITLE, ElementAttribute.NAME)
        assert ios_profile.profile_img_profile.exists()
        expect(ios_profile.profile_user_name_text).to_have(values.PROFILE_NAME_TEXT)
        expect(ios_profile.profile_user_username_text).to_have(values.PROFILE_USERNAME_TEXT)
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT)
        assert ios_profile.edit_profile_title.exists()
