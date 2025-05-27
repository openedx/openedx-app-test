"""
Course Dashboard Screen Test Module
"""

import pytest

from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_landing import IosLanding
from tests.common import values
from tests.common.globals import Globals


@pytest.mark.IOS
class TestIosCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify that clicking course from Main dashboard load course dashboard,
            Verify that Course Dashboard tab will show following contents,
            Header contents,
                Back icon,
                Specific "<course name>" as Title, Share icon, Course,
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Handouts" tab will load Handouts screen
            Verify on tapping "Announcements" tab will load Announcements screen
            Verify on tapping "Home" tab will load Home screen
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        course_dashboard_page = IosCourseDashboard()
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding()

        second_course_name = global_contents.get_element_by_name_ios(driver, values.MAIN_DASHBOARD_COURSE_NAME)

        second_course_name.click()
        if ios_landing.allow_notifications_button.exists(raise_exception=False):
            ios_landing.allow_notifications_button.click()

        course_tab = course_dashboard_page.course_dashboard_course_tab
        expect(course_tab).to_have(second_course_name.text)

        videos_tab = course_dashboard_page.course_dashboard_videos_tab
        expect(videos_tab).to_have(values.COURSE_DASHBOARD_VIDEOS_TAB)
        videos_tab.click()

        discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
        expect(discussions_tab).to_have(values.COURSE_DASHBOARD_DISCUSSIONS_TAB)
        assert discussions_tab.click()

        dates_tab = course_dashboard_page.course_dashboard_dates_tab
        expect(dates_tab).to_have(values.COURSE_DASHBOARD_DATES_TAB)
        assert dates_tab.click()

        more_tab = course_dashboard_page.course_dashboard_more_tab
        expect(more_tab).to_have(values.COURSE_DASHBOARD_MORE_TAB)
        assert more_tab.click()

        dashboard_tab = course_dashboard_page.back_navigation_button
        expect(dashboard_tab).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
        assert dashboard_tab.click()
