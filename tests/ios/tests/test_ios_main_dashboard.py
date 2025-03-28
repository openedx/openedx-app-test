"""
    Main Dashboard Test Module
"""

from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages import ios_elements


class TestIosMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_ui_elements_smoke(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen,
                Screen Title, Discover Tab
                Profile Tab, Programs Tab, Profile tab
            Verify that Discover tab will be selected by default
            Verify that clicking each tab will load its screen
        """

        driver = ios_login

        main_dashboard = IosMainDashboard(driver, setup_logging)
        learn_tab = main_dashboard.get_main_dashboard_learn_tab()
        learn_tab.click()
        assert learn_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        discover_tab = main_dashboard.get_main_dashboard_discover_tab()
        discover_tab.click()
        assert discover_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()

    def test_validate_programs_switcher(self, set_capabilities, setup_logging):
        """
         Scenarios:
            Verify following contents are visible on screen,
                Courses switcher
                Profile Tab, Programs Tab, Profiel tab
            Verify that clicking courses switcher will open dropdown
            Verify that dropdown has courses and programs options in it
            Verify that clicking each menu will load its screen
        """

        global_contents = Globals(setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)
        learn_tab = main_dashboard.get_main_dashboard_learn_tab()
        learn_tab.click()
        switcher_label = global_contents.wait_and_get_element(set_capabilities, ios_elements.main_dashboard_dropdown_text)
        assert switcher_label.get_attribute('label') == 'Courses'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'Courses')
        assert switcher_label.get_attribute('label') == 'Courses'
        programs_switcher = global_contents.wait_and_get_element(set_capabilities, 'Programs')
        assert programs_switcher.text == 'Programs'
        course_switcher.click()
        assert switcher_label.get_attribute('label') == 'Courses'
        switcher_label.click()
        programs_switcher = global_contents.wait_and_get_element(set_capabilities, 'Programs')
        programs_switcher.click()
        assert switcher_label.get_attribute('label') == 'Programs'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'Courses')
        course_switcher.click()
        assert switcher_label.get_attribute('label') == 'Courses'
