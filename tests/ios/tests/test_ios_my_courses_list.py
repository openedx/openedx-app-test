"""
    My Courses List Test Module
"""

from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_profile import IosProfile
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

        assert my_courses_list.get_all_courses_header_text().text == values.ALL_COURSES_HEADER_LABEL
        assert my_courses_list.get_all_courses_label().text == values.ALL_COURSES_LABEL
        my_courses_list.get_all_courses_label().click()
        all_enrolled_courses = global_contents.get_elements_by_name_ios(set_capabilities , 'course_item')
        assert len(all_enrolled_courses) == 3

        assert my_courses_list.get_all_courses_inprogress_label().text == values.ALL_COURSES_INPROGRESS_LABEL
        my_courses_list.get_all_courses_inprogress_label().click()
        in_progress_courses = global_contents.get_elements_by_name_ios(set_capabilities, 'course_item')
        assert len(in_progress_courses) == 3

        assert my_courses_list.get_all_courses_completed_label().text == values.ALL_COURSES_COMPLETED_LABEL
        my_courses_list.get_all_courses_completed_label().click()
        completed_courses = global_contents.get_element_by_name_ios(set_capabilities, 'No Completed Courses')
        assert completed_courses.text == 'No Completed Courses'

        assert my_courses_list.get_all_courses_expired_label().text == values.ALL_COURSES_EXPIRED_LABEL
        my_courses_list.get_all_courses_expired_label().click()
        expired_courses = global_contents.get_element_by_name_ios(set_capabilities, 'No Expired Courses')
        assert expired_courses.text == 'No Expired Courses'

        dashboard_tab = course_dashboard_page.navigate_to_main_dashboard_tab()
        assert dashboard_tab.get_attribute('label') == values.LANDING_BACK_BUTTON
        dashboard_tab.click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE
        assert ios_profile.get_profile_settings_button().text == values.PROFILE_SETTINGS_TEXT
        ios_profile.get_profile_settings_button().click()
        assert ios_profile.get_profile_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_profile_logout_button().click()
        assert ios_profile.get_logout_close_button().text == 'Close'
        assert ios_profile.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        assert ios_profile.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_logout_button().click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE_IOS
