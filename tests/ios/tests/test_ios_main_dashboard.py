"""
    Main Dashboard Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
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
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        main_dashboard = IosMainDashboard()
        learn_tab = main_dashboard.get_main_dashboard_learn_tab
        assert learn_tab.click()
        expect(learn_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

        discover_tab = main_dashboard.main_dashboard_discover_tab
        assert discover_tab.click()
        expect(discover_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

        profile_tab = main_dashboard.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB)
        assert profile_tab.click()

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        main_dashboard = IosMainDashboard()
        learn_tab = main_dashboard.get_main_dashboard_learn_tab
        assert learn_tab.click()
        switcher_label = global_contents.wait_and_get_element(set_capabilities, ios_elements.main_dashboard_dropdown_text)
        assert switcher_label.get_attribute('label') == 'Courses'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(
            set_capabilities, "Courses"
        )
        assert switcher_label.get_attribute("label") == "Courses"
        programs_switcher = global_contents.wait_and_get_element(
            set_capabilities, "Programs"
        )
        assert programs_switcher.text == "Programs"
        course_switcher.click()
        assert switcher_label.get_attribute("label") == "Courses"
        switcher_label.click()
        programs_switcher = global_contents.wait_and_get_element(
            set_capabilities, "Programs"
        )
        programs_switcher.click()
        assert switcher_label.get_attribute("label") == "Programs"
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(
            set_capabilities, "Courses"
        )
        course_switcher.click()
        assert switcher_label.get_attribute("label") == "Courses"
