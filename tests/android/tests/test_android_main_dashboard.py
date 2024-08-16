"""
    Main Dashboard Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import values
from tests.common.globals import Globals
from tests.android.pages.android_sign_in import AndroidSignIn


class TestAndroidMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidMainDashboard.__name__} Test Case')
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

        learn_tab = main_dashboard_page.get_learn_tab()
        assert learn_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        discover_tab = main_dashboard_page.get_discover_tab()
        assert discover_tab.get_attribute('content-desc') == values.DISCOVER_SCREEN_HEADING
        assert discover_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        assert profile_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        profile_tab.click()
        assert profile_tab.get_attribute('selected') == values.TRUE_LOWERCASE
        main_dashboard_page.get_learn_tab().click()

    def test_validate_programs_switcher(self, set_capabilities, setup_logging):
        """
         Scenarios:
            Verify following contents are visible on screen, 
                Courses switcher
                Profile Tab, Programs Tab, Profiel tab
            Verify that clicking courses switcher will open dropdown
            Verify that dropdown has courses and programs options in it
            Verify that clicking each menu will load its screen
        """

        global_contents = Globals(setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)

        switcher_label = global_contents.get_element_by_text(set_capabilities, 'Courses')
        assert switcher_label
        switcher_label.click()
        course_switcher = android_sign_in.get_all_textviews()[0]
        assert course_switcher.text == 'Courses'
        programs_switcher = android_sign_in.get_all_textviews()[1]
        assert programs_switcher.text == 'Programs'
        course_switcher.click()

        switcher_label = global_contents.get_element_by_text(set_capabilities, 'Courses')
        assert switcher_label
        switcher_label.click()
        programs_switcher = android_sign_in.get_all_textviews()[1]
        programs_switcher.click()
        assert global_contents.get_element_by_text(set_capabilities, 'Programs')

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
        assert profile_page.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
