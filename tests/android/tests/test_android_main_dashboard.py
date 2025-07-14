"""
Main Dashboard Test Module
"""

import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.enums.attributes import ElementAttribute


@pytest.mark.ANDROID
@pytest.mark.SMOKE
class TestAndroidMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
        Scenarios:
           Verify following contents are visible on screen,
               Screen Title, Discover Tab
               Profile Tab, Programs Tab, Profile tab
           Verify that Discover tab will be selected by default
           Verify that clicking each tab will load its screen
        """

        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()

        learn_tab = main_dashboard_page.learn_tab
        expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
        expect(learn_tab).to_be_selected()

        discover_tab = main_dashboard_page.discover_tab
        expect(discover_tab).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.CONTENT_DESC)
        expect(discover_tab).not_.to_be_selected()
        assert discover_tab.click()
        expect(discover_tab).to_be_selected()

        profile_tab = main_dashboard_page.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.CONTENT_DESC)
        expect(profile_tab).not_.to_be_selected()
        assert profile_tab.click()
        expect(profile_tab).to_be_selected()
        assert main_dashboard_page.learn_tab.click()

    def test_validate_programs_switcher(self, android_login, setup_logging):
        """
        Scenarios:
           Verify following contents are visible on screen,
               Courses switcher
               Profile Tab, Programs Tab, Profile tab
           Verify that clicking courses switcher will open dropdown
           Verify that dropdown has courses and programs options in it
           Verify that clicking each menu will load its screen
        """

        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        main_dashboard = AndroidMainDashboard()

        assert main_dashboard.switcher_label_courses.exists()
        assert main_dashboard.switcher_label_courses.click()
        assert main_dashboard.find_by_text_on_screen("Courses")
        assert main_dashboard.find_by_text_on_screen("Programs")
        assert main_dashboard.find_by_text_on_screen("Courses").click()
        assert main_dashboard.switcher_label_courses.exists()
        assert main_dashboard.switcher_label_courses.click()
        assert main_dashboard.find_by_text_on_screen("Programs").click()
        assert main_dashboard.switcher_label_programs.exists()
