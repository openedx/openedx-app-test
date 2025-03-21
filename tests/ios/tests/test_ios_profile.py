"""
    Profile Screen Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestIosProfile:
    """
    Profile screen's Test Case
    """

    def test_start_profile_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Profile is loaded successfully
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f'Starting {TestIosProfile.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew()
        main_dashboard = IosMainDashboard()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.whats_new_next_button.click()
            setup_logging.info('Whats New screen is successfully loaded')

        profile_tab = main_dashboard.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB)
        assert profile_tab.click()

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
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
        ios_profile = IosProfile()
        expect(ios_profile.navigation_bar_title).to_have(values.PROFILE_SCREEN_TITLE, ElementAttribute.NAME)
        assert ios_profile.profile_img_profile.exists()
        expect(ios_profile.profile_user_name_text).to_have(values.PROFILE_NAME_TEXT)
        expect(ios_profile.profile_user_username_text).to_have(values.PROFILE_USERNAME_TEXT)
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT)
        assert ios_profile.edit_profile_title.exists()