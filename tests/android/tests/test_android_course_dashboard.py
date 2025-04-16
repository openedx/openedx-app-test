"""
Course Dashboard Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.common import values


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
        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        course_dashboard_page = AndroidCourseDashboard()

        second_course_name = course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
        assert second_course_name.click()
        if course_dashboard_page.allow_notifications_button:
            assert course_dashboard_page.allow_notifications_button.click()

        expect(course_dashboard_page.course_dashboard_home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)

        videos_tab = course_dashboard_page.course_dashboard_videos_tab
        expect(videos_tab).to_have(values.COURSE_DASHBOARD_VIDEOS_TAB)
        assert videos_tab.click()

        discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
        expect(discussions_tab).to_have(values.COURSE_DASHBOARD_DISCUSSIONS_TAB)
        assert discussions_tab.click()

        dates_tab = course_dashboard_page.course_dashboard_dates_tab
        expect(dates_tab).to_have(values.COURSE_DASHBOARD_DATES_TAB)
        assert dates_tab.click()

        more_tab = course_dashboard_page.course_dashboard_more_tab
        expect(more_tab).to_have(values.COURSE_DASHBOARD_MORE_TAB)
        assert more_tab.click()

        assert course_dashboard_page.back_button.click()
