"""
    My Courses Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidMyCoursesList:
    """
    My Courses screen's Test Case
    """

    def test_start_my_courses_list_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidMyCoursesList.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_done_button().click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
         Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
            Verify that My Courses(enrolled) List with followings in each course,
                Course image
                Course Name
                Course Start/End date
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
        """

        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        my_courses_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        learn_tab = main_dashboard_page.get_learn_tab()
        assert learn_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        assert my_courses_page.get_my_course_toolbar_title().text == values.MAIN_DASHBOARD_DASHBOARD_TAB
        assert my_courses_page.get_my_course_screen_title().text == values.MAIN_DASHBOARD_COURSES
        assert my_courses_page.get_my_courses_description().text == values.MAIN_DASHBOARD_COURSE_DESCRIPTION
        assert my_courses_page.get_my_courses_org_name().text == values.MAIN_DASHBOARD_COURSE_ORG
        assert my_courses_page.get_my_courses_course_date()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        profile_page.get_settings_button().click()
        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())
        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
