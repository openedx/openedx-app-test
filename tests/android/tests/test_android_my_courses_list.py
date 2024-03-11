"""
    My Courses Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
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
            Verify following contents are visible on screen, 
                Screen Title, Disover Tab
                Profile Tab, Programs Tab, Profiel tab
            Verify that Discover tab will be selected by default
            Verify that clicking each tab will load its screen
        """

        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        my_courses_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        dashboard_tab = main_dashboard_page.get_dashboard_tab()
        assert dashboard_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_DASHBOARD_TAB
        dashboard_tab.click()
        assert dashboard_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        assert my_courses_page.get_my_course_toolbar_title().text == values.MAIN_DASHBOARD_DASHBOARD_TAB
        assert my_courses_page.get_my_course_screen_title().text == values.MAIN_DASHBOARD_COURSES
        assert my_courses_page.get_my_courses_description().text == values.MAIN_DASHBOARD_COURSE_DESCRIPTION
        assert my_courses_page.get_my_courses_org_name().text == values.MAIN_DASHBOARD_COURSE_ORG
        assert my_courses_page.get_my_courses_course_date()
