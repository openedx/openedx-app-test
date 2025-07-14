"""
My Courses Test Module
"""

import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.enums.attributes import ElementAttribute


@pytest.mark.ANDROID
@pytest.mark.SMOKE
class TestAndroidMyCoursesList:
    """
    My Courses screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
        Scenarios:
           Verify that from Main Dashboard tapping Courses tab will load My Courses
           list(of specific logged-in user) in its tab
           Verify that Courses tab/screen will show following header contents,
           Header Contents
               Learn
           Verify that My Courses(enrolled) List with followings in each course,
               Progress bar
               Organization
               Name
               Start/End date
               Due date
               Resume label
               Second Course
               Third Course
           Verify that tapping any course should load specific Course Dashboard screen
           Verity that from Course Dashboard tapping back should load My Courses List screen
        """
        main_dashboard_page = AndroidMainDashboard()
        course_dashboard = AndroidCourseDashboard()

        learn_tab = main_dashboard_page.learn_tab

        expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
        expect(learn_tab).to_be_selected()
        course_view = course_dashboard.course_view
        expect(course_view).to_be_displayed()
        expect(course_dashboard.course_progress_bar_view).to_have("0.0")
        text_views = course_dashboard.get_all_text_views_inside_course_view()
        assert course_dashboard.find_by_text_on_screen(values.MAIN_DASHBOARD_COURSE_ORG)
        assert course_dashboard.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
        expect(text_views[3]).to_match(r".+")
        expect(text_views[4]).to_match(r".+")
        assert course_dashboard.find_by_text_on_screen(values.MAIN_DASHBOARD_RESUME_LABEL)
        expect(text_views[6]).to_match(r".+")

    def test_view_all_courses(self, android_login, setup_logging):
        """
        Scenarios:
            Verify that tapping View All My Courses label should load My Courses List screen
            Verify All Courses  label should be displayed
            Verify that tapping All label should load all enrolled courses
            Verify that tapping In Progress label should load all in progress courses
            Verify that tapping Completed label should load all completed courses
            Verify that tapping Expired label should load all expired courses
            Verify that tapping back button should load Main Dashboard screen
        """

        pytest.skip("Need another test course to perform these assertions")

        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        course_dashboard = AndroidCourseDashboard()

        text_views = course_dashboard.get_all_text_views_inside_course_view()
        expect(text_views[8]).to_contain(values.MAIN_DASHBOARD_ALL_COURSES_LABEL)
        assert text_views[8].click()

        assert course_dashboard.all_courses_label.exists()

        assert course_dashboard.all_label.exists()
        assert course_dashboard.all_label.click()
        assert course_dashboard.all_progress_bar_views().count() == 3
        assert course_dashboard.in_progress.exists()
        assert course_dashboard.in_progress.click()
        assert course_dashboard.all_progress_bar_views().count() == 3
        assert course_dashboard.completed_course.exists()
        assert course_dashboard.completed_course.click()
        expect(course_dashboard.empty_state_title).to_have("No Completed Courses")
        assert course_dashboard.expired_courses.exists()
        assert course_dashboard.expired_courses.click()
        assert course_dashboard.learn_online_label.exists()
        assert expect(course_dashboard.empty_state_title).to_have("No Expired Courses")
        assert course_dashboard.back_navigation_button.click()
