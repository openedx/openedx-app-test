"""
    My Courses List Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.common.enums.general_enums import IosClassViews
from tests.ios.pages.ios_landing import IosLanding
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f'Starting {TestIosMyCoursesList.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.whats_new_next_button.click()
            setup_logging.info('Whats New screen is successfully loaded')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        my_courses_list = IosMyCoursesList()
        expect(my_courses_list.my_courses_header_text).to_have(values.MAIN_DASHBOARD_LEARN_TAB)
        expect(my_courses_list.get_my_course_image).to_be_visible()
        expect(my_courses_list.get_my_course_org_text).to_have(values.MAIN_DASHBOARD_COURSE_ORG)
        expect(my_courses_list.get_my_course_name_text).to_have(values.MAIN_DASHBOARD_COURSE_NAME)
        buttons = IosMyCoursesList.find_all_views_on_screen(IosClassViews.BUTTON)
        due_assignment = buttons[5]
        expect(due_assignment).to_contain('Assignments')
        resume_course = buttons[6]
        expect(resume_course).to_contain('Resume')
        second_course = buttons[8]
        expect(second_course).to_have(values.MAIN_DASHBOARD_COURSE_NAME)
        third_course = buttons[9]
        expect(third_course).to_have('How to Learn Online')
        expect(my_courses_list.my_courses_welcome_back_text).to_contain(values.MAIN_DASHBOARD_COURSE_DESCRIPTION)
        assert my_courses_list.my_courses_welcome_back_text.click()

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        my_courses_list = IosMyCoursesList()
        course_dashboard_page = IosCourseDashboard()

        expect(my_courses_list.get_all_courses_header_text).to_have(values.ALL_COURSES_HEADER_LABEL)
        expect(my_courses_list.get_all_courses_label).to_have(values.ALL_COURSES_LABEL)
        assert my_courses_list.get_all_courses_label.click()
        all_enrolled_courses = global_contents.get_elements_by_name_ios(set_capabilities , 'course_item')
        assert len(all_enrolled_courses) == 3

        expect(my_courses_list.all_courses_in_progress_label).to_have(values.ALL_COURSES_INPROGRESS_LABEL)
        assert my_courses_list.all_courses_in_progress_label.click()
        in_progress_courses = global_contents.get_elements_by_name_ios(set_capabilities, 'course_item')
        assert len(in_progress_courses) == 2

        expect(my_courses_list.get_all_courses_completed_label).to_have(values.ALL_COURSES_COMPLETED_LABEL)
        assert my_courses_list.get_all_courses_completed_label.click()
        completed_courses = global_contents.get_element_by_name_ios(set_capabilities, 'No Completed Courses')
        assert completed_courses.text == 'No Completed Courses'

        expect(my_courses_list.get_all_courses_expired_label).to_have(values.ALL_COURSES_EXPIRED_LABEL)
        assert my_courses_list.get_all_courses_expired_label.click()
        expired_courses = global_contents.get_element_by_name_ios(set_capabilities, 'How to Learn Online')
        assert expired_courses.text == 'How to Learn Online'

        dashboard_tab = course_dashboard_page.back_navigation_button
        expect(dashboard_tab).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
        assert dashboard_tab.click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should log out from main dashboard screen
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_profile = IosProfile()
        ios_landing = IosLanding()
        main_dashboard = IosMainDashboard()

        profile_tab = main_dashboard.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB)
        assert profile_tab.click()
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT)
        assert ios_profile.profile_settings_button.click()
        expect(ios_profile.get_profile_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON, case='lower')
        assert ios_profile.get_profile_logout_button.click()
        expect(ios_profile.get_logout_close_button).to_have('Close')
        expect(ios_profile.get_logout_dialog_title).to_have(values.LOGOUT_DIALOG_TITLE)
        expect(ios_profile.get_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON, case='lower')
        assert ios_profile.get_logout_button.click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE
