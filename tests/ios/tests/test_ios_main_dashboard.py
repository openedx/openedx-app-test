"""
Main Dashboard Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew


@pytest.mark.IOS
@pytest.mark.IOS_SMOKE
class TestIosMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_ios_main_dashboard(self, ios_login, setup_logging):
        """
        Scenarios:
            1. Dismiss "What’s New" screen if it appears.
               - Verify Learn tab is loaded.
               - Verify tab bar exists with the following options:
               * Learn
               * Discover
               * Profile
               - Verify icons if possible.

            2. Click on Discover tab.
               - Verify Discover tab is selected.
               - Verify screen title is "Discover".
               - Verify Discover page heading title is:
             "Build skills. Earn a certificate. Advance your career".

            3. Click on Profile tab.
               - Verify Profile screen is loaded with title "Profile".
               - Verify username and full name.
               - Verify settings icon and Edit Profile button exist.

            4. Click on Learn tab.
               - Verify heading is "Learn".
               - Verify courses dropdown exists.
               - Verify "demoX" course is displayed.
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        whats_new_page = IosWhatsNew()
        main_dashboard = IosMainDashboard()
        my_courses_list = IosMyCoursesList()
        ios_discover_page = IosDiscoverPage()
        ios_profile = IosProfile()
        global_contents = Globals(setup_logging)

        with allure.step("Dismiss 'What’s New' screen if it appears."):
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()

        with allure.step("Verify Learn tab is loaded."):
            expect(main_dashboard.learn_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)
            expect(my_courses_list.my_courses_header_text).to_have(
                values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.LABEL
            )

        with allure.step("Verify tab bar exists with the following options: Learn, Discover, Profile."):
            expect(main_dashboard.tab_bar).to_be_visible()
            expect(main_dashboard.learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.LABEL)
            expect(main_dashboard.main_dashboard_discover_tab).to_have(
                values.MAIN_DASHBOARD_DISCOVER_TAB, ElementAttribute.LABEL
            )
            expect(main_dashboard.profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.LABEL)

        with allure.step("Click on Discover tab."):
            main_dashboard.main_dashboard_discover_tab.click()
            expect(main_dashboard.main_dashboard_discover_tab_selected).to_have(
                values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE
            )
            expect(main_dashboard.navigation_bar_title).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME)
            expect(ios_discover_page.heading_title_part1).to_have(
                values.DISCOVER_SCREEN_HEADING_PART1, ElementAttribute.LABEL
            )
            expect(ios_discover_page.heading_title_part2).to_have(
                values.DISCOVER_SCREEN_HEADING_PART2, ElementAttribute.LABEL
            )

        with allure.step("Click on Profile tab."):
            main_dashboard.profile_tab.click()
            expect(main_dashboard.navigation_bar_title).to_have(values.PROFILE_SCREEN_TITLE, ElementAttribute.NAME)
            expect(ios_profile.full_name_label).to_have(values.PROFILE_NAME_TEXT, ElementAttribute.LABEL)
            expect(ios_profile.username_label).to_have(f"@{global_contents.login_user_name}", ElementAttribute.LABEL)
            expect(ios_profile.find_by_text_on_screen(values.PROFILE_SETTINGS_TEXT)).to_be_visible()
            expect(ios_profile.edit_profile_button).to_be_visible()

        with allure.step("Click on Learn tab."):
            main_dashboard.learn_tab.click()
            expect(my_courses_list.courses_dropdown_menu).to_have(values.MAIN_DASHBOARD_COURSES, ElementAttribute.LABEL)
            expect(my_courses_list.course_demoX).to_have(values.MY_COURSES_SECOND_COURSE_NAME, ElementAttribute.LABEL)
