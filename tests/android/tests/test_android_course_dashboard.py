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

        learn_tab = main_dashboard_page.get_learn_tab()
        assert learn_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == values.TRUE_LOWERCASE

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
            Verify on tapping "Home" tab will load Home screen
        """

        course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        second_course_name = global_contents.get_element_by_text(set_capabilities, values.MY_COURSES_SECOND_COURSE_NAME)
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

        set_capabilities.back()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        profile_tab.click()
        profile_page.get_settings_button().click()
        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())

        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
