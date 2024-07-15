"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_start_course_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidCourseDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_done_button().click()

        dashboard_tab = main_dashboard_page.get_dashboard_tab()
        assert dashboard_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_DASHBOARD_TAB
        dashboard_tab.click()
        assert dashboard_tab.get_attribute('selected') == values.TRUE_LOWERCASE

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
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

        course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        second_course = course_dashboard_page.get_my_courses_list(set_capabilities)[1]
        second_course_name = global_contents.get_child_element(second_course, android_elements.my_courses_course_name)
        # second_course = course_dashboard_page.get_my_courses_list()[1]
        second_course_name = global_contents.get_element_by_text(set_capabilities, values.MY_COURSES_SECOND_COURSE_NAME)
        # second_course_name = global_contents.get_child_element(second_course, android_elements.my_courses_course_name)

        assert second_course_name.text == values.MY_COURSES_SECOND_COURSE_NAME
        second_course_name.click()

        course_tab = course_dashboard_page.get_course_dashboard_course_tab()
        assert course_tab.get_attribute('content-desc') == values.COURSE_DASHBOARD_COURSE_TAB
        assert course_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        videos_tab = course_dashboard_page.get_course_dashboard_videos_tab()
        assert videos_tab.get_attribute('content-desc') == values.COURSE_DASHBOARD_VIDEOS_TAB
        assert videos_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        videos_tab.click()
        assert videos_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        discussions_tab = course_dashboard_page.get_course_dashboard_discussions_tab()
        assert discussions_tab.get_attribute('content-desc') == values.COURSE_DASHBOARD_DISCUSSIONS_TAB
        assert discussions_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        discussions_tab.click()
        assert discussions_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        dates_tab = course_dashboard_page.get_course_dashboard_dates_tab()
        assert dates_tab.get_attribute('content-desc') == values.COURSE_DASHBOARD_DATES_TAB
        assert dates_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        dates_tab.click()
        assert dates_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        handouts_tab = course_dashboard_page.get_course_dashboard_resources_tab()
        assert handouts_tab.get_attribute('content-desc') == values.COURSE_DASHBOARD_RESOURCES_TAB
        assert handouts_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        handouts_tab.click()
        assert handouts_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        back_button = course_dashboard_page.get_back_button()
        assert back_button.get_attribute('content-desc') == values.BACK_BUTTON_SMALL
        back_button.click()

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

        assert profile_page.get_logout_dialog_title() == values.TRUE_LOWERCASE
        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())

        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
