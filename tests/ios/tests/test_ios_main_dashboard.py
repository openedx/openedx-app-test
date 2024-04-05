"""
    Main Dashboard Test Module
"""

from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestIosMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard is loaded successfully
        """

        setup_logging.info(f'Starting {TestIosMainDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen, 
                Screen Title, Disover Tab
                Profile Tab, Programs Tab, Profiel tab
            Verify that Discover tab will be selected by default
            Verify that clicking each tab will load its screen
        """

        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)
        discover_tab = main_dashboard.get_main_dashboard_discover_tab()
        assert discover_tab.text == values.DISCOVER_SCREEN_HEADING
        discover_tab.click()
        assert discover_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        dashboard_tab = main_dashboard.get_main_dashboard_tab()
        assert dashboard_tab.get_attribute('name') == values.MAIN_DASHBOARD_DASHBOARD_TAB
        dashboard_tab.click()
        assert dashboard_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        programs_tab = main_dashboard.get_main_dashboard_programs_tab()
        assert programs_tab.text == values.MAIN_DASHBOARD_PROGRAMS_TAB
        programs_tab.click()
        assert programs_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        setup_logging.info('All tabs are successfully loaded')
