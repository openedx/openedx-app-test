"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.common import values
from tests.common.globals import Globals


class TestAndroidCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
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
            Verify on tapping "Home" tab will load Home screen
        """
        driver = android_login
        course_dashboard_page = AndroidCourseDashboard(driver, setup_logging)
        global_contents = Globals(setup_logging)
        second_course_name = global_contents.get_element_by_text(driver, values.MY_COURSES_SECOND_COURSE_NAME)
        assert second_course_name.text == values.MY_COURSES_SECOND_COURSE_NAME
        second_course_name.click()
        if course_dashboard_page.get_allow_notifications_button():
            course_dashboard_page.get_allow_notifications_button().click()

        home_tab = course_dashboard_page.get_course_dashboard_home_tab()
        assert home_tab.text == values.COURSE_DASHBOARD_HOME_TAB

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

        driver.back()
