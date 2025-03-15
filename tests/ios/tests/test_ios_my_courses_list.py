"""
    My Courses List Test Module
"""

from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.common import values
from tests.common.globals import Globals


class TestIosMyCoursesList:
    """
    My Courses List screen's Test Case
    """

    def test_ui_elements_smoke(self, ios_login, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged-in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
            Verify that My Courses(enrolled) List with followings in each course,
                Course Image
                Course Name
                Course Start/End date
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
        """
        driver = ios_login
        my_courses_list = IosMyCoursesList(driver, setup_logging)
        assert my_courses_list.get_my_courses_header_text().text == values.MAIN_DASHBOARD_LEARN_TAB
        assert my_courses_list.get_my_course_image().get_attribute('visible') == values.TRUE_LOWERCASE
        assert my_courses_list.get_my_course_org_text().text == values.MAIN_DASHBOARD_COURSE_ORG
        assert my_courses_list.get_my_course_name_text().text == values.MAIN_DASHBOARD_COURSE_NAME
        # assert 'Ends' in my_courses_list.get_my_course_end_text().text
        buttons = my_courses_list.get_all_buttons()

        due_assignment = buttons[5]
        assert "Assignments" in due_assignment.text
        resume_course = buttons[6]
        assert "Resume" in resume_course.text
        second_course = buttons[8]
        assert second_course.text == values.MAIN_DASHBOARD_COURSE_NAME
        third_course = buttons[9]
        assert third_course.text == "How to Learn Online"
        assert (
            values.MAIN_DASHBOARD_COURSE_DESCRIPTION
            in my_courses_list.get_my_courses_welcomeback_text().text
        )
        my_courses_list.get_my_courses_welcomeback_text().click()

    def test_view_all_courses(self, set_capabilities, setup_logging):
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

        global_contents = Globals(setup_logging)
        my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        assert (
            my_courses_list.get_all_courses_header_text().text
            == values.ALL_COURSES_HEADER_LABEL
        )
        assert my_courses_list.get_all_courses_label().text == values.ALL_COURSES_LABEL
        my_courses_list.get_all_courses_label().click()
        all_enrolled_courses = global_contents.get_elements_by_name_ios(
            set_capabilities, "course_item"
        )
        assert len(all_enrolled_courses) == 3

        assert (
            my_courses_list.get_all_courses_inprogress_label().text
            == values.ALL_COURSES_INPROGRESS_LABEL
        )
        my_courses_list.get_all_courses_inprogress_label().click()
        in_progress_courses = global_contents.get_elements_by_name_ios(
            set_capabilities, "course_item"
        )
        assert len(in_progress_courses) == 2

        assert (
            my_courses_list.get_all_courses_completed_label().text
            == values.ALL_COURSES_COMPLETED_LABEL
        )
        my_courses_list.get_all_courses_completed_label().click()
        completed_courses = global_contents.get_element_by_name_ios(
            set_capabilities, "No Completed Courses"
        )
        assert completed_courses.text == "No Completed Courses"

        assert (
            my_courses_list.get_all_courses_expired_label().text
            == values.ALL_COURSES_EXPIRED_LABEL
        )
        my_courses_list.get_all_courses_expired_label().click()
        expired_courses = global_contents.get_element_by_name_ios(
            set_capabilities, "How to Learn Online"
        )
        assert expired_courses.text == "How to Learn Online"

        dashboard_tab = course_dashboard_page.navigate_to_main_dashboard_tab()
        assert dashboard_tab.get_attribute("label") == values.LANDING_BACK_BUTTON
        dashboard_tab.click()
