"""
    My Courses List Test Module
"""

from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestIosMyCoursesList:
    """
    My Courses List screen's Test Case
    """

    def test_start_my_courses_list_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify My Courses list screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestIosMyCoursesList.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged in user) in its tab
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

        my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        assert my_courses_list.get_my_courses_header_text().text == values.MAIN_DASHBOARD_LEARN_TAB
        assert my_courses_list.get_my_course_image().get_attribute('visible') == values.TRUE_LOWERCASE
        assert my_courses_list.get_my_course_org_text().text == values.MAIN_DASHBOARD_COURSE_ORG
        assert my_courses_list.get_my_course_name_text().text == values.MAIN_DASHBOARD_COURSE_NAME
        assert 'Ends' in my_courses_list.get_my_course_end_text().text
        buttons = my_courses_list.get_all_buttons()

        due_assignment = buttons[5]
        assert 'Assignments' in due_assignment.text
        resume_course = buttons[6]
        assert 'Resume' in resume_course.text
        second_course = buttons[8]
        assert second_course.text == values.MY_COURSES_SECOND_COURSE_NAME
        third_course = buttons[9]
        assert third_course.text == 'How to Learn Online'
        assert values.MAIN_DASHBOARD_COURSE_DESCRIPTION in my_courses_list.get_my_courses_welcomeback_text().text
        my_courses_list.get_my_courses_welcomeback_text().click()
