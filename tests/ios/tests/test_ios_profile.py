"""
    Profile Screen Test Module
"""

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

        setup_logging.info(f'Starting {TestIosProfile.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon 
                "Profile" as Title
                Edit Profile Button
                Profile Image
                User Name
                Video Settings
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert global_contents.get_navigation_bar_title(set_capabilities)[0].get_attribute(
            'name') == values.PROFILE_SCREEN_TITLE
        assert ios_profile.get_profile_img_profile()
        assert ios_profile.get_profile_user_name_text().text == values.PROFILE_NAME_TEXT
        assert ios_profile.profile_user_username_text().text == values.PROFILE_USERNAME_TEXT
        assert ios_profile.get_profile_settings_button().text == values.PROFILE_SETTINGS_TEXT
        assert global_contents.get_element_by_name_ios(set_capabilities,
                                                       values.EDIT_PROFILE_TITLE).text == values.EDIT_PROFILE_TITLE
