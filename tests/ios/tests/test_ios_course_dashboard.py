"""
    Course Dashboard Screen Test Module
"""

from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_landing import IosLanding
from tests.common import values
from tests.common.globals import Globals


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
        course_dashboard_page = IosCourseDashboard(driver, setup_logging)
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding(driver, setup_logging)

        second_course_name = global_contents.get_element_by_name_ios(driver, values.MAIN_DASHBOARD_COURSE_NAME)

        second_course_name.click()
        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()

        course_tab = course_dashboard_page.get_course_dashboard_course_tab()
        assert course_tab.text == values.COURSE_DASHBOARD_HOME_TAB

        videos_tab = course_dashboard_page.get_course_dashboard_videos_tab()
        assert videos_tab.text == values.COURSE_DASHBOARD_VIDEOS_TAB
        videos_tab.click()

        discussions_tab = course_dashboard_page.get_course_dashboard_discussions_tab()
        assert discussions_tab.text == values.COURSE_DASHBOARD_DISCUSSIONS_TAB
        discussions_tab.click()

        dates_tab = course_dashboard_page.get_course_dashboard_dates_tab()
        assert dates_tab.text == values.COURSE_DASHBOARD_DATES_TAB
        dates_tab.click()

        more_tab = course_dashboard_page.get_course_dashboard_more_tab()
        assert more_tab.text == values.COURSE_DASHBOARD_MORE_TAB
        more_tab.click()

        dashboard_tab = course_dashboard_page.navigate_to_main_dashboard_tab()
        assert dashboard_tab.get_attribute('label') == values.LANDING_BACK_BUTTON
        dashboard_tab.click()
