
"""
    Profile Screen Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        whats_new_page = AndroidWhatsNew()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.done_button.click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()

        expect(main_dashboard_page.profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, attribute=ElementAttribute.CONTENT_DESC)
        expect(main_dashboard_page.profile_tab).to_not.to_be_selected()
        assert main_dashboard_page.profile_tab.click()
        assert profile_page.settings_button.exists()
        expect(profile_page.profile_img_profile).to_contain(values.PROFILE_IMAGE_TEXT, type=ElementAttribute.CONTENT_DESC)
        expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)
        expect(profile_page.profile_username).to_have(values.PROFILE_USERNAME_TEXT)
        expect(profile_page.edit_profile_button).to_have(values.EDIT_PROFILE_TITLE)
