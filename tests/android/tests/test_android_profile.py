"""
Profile Screen Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.common.enums.attributes import ElementAttribute


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
        driver = android_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()

        expect(main_dashboard_page.profile_tab).to_have(
            values.MAIN_DASHBOARD_PROFILE_TAB, attribute=ElementAttribute.CONTENT_DESC
        )
        expect(main_dashboard_page.profile_tab).not_.to_be_selected()
        assert main_dashboard_page.profile_tab.click()
        assert profile_page.settings_button.exists()
        expect(profile_page.profile_img_profile).to_contain(
            values.PROFILE_IMAGE_TEXT, attribute=ElementAttribute.CONTENT_DESC
        )
        expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)
        expect(profile_page.profile_username).to_have(values.PROFILE_USERNAME_TEXT)
        expect(profile_page.edit_profile_button).to_have(values.EDIT_PROFILE_TITLE)
