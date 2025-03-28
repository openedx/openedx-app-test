"""
    Main Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.globals import Globals
from tests.android.pages.android_sign_in import AndroidSignIn


class TestAndroidMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
         Scenarios:
            Verify following contents are visible on screen, 
                Screen Title, Discover Tab
                Profile Tab, Programs Tab, Profile tab
            Verify that Discover tab will be selected by default
            Verify that clicking each tab will load its screen
        """
        driver = android_login
        main_dashboard_page = AndroidMainDashboard(driver, setup_logging)

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

    def test_validate_programs_switcher(self, android_login, setup_logging):
        """
         Scenarios:
            Verify following contents are visible on screen, 
                Courses switcher
                Profile Tab, Programs Tab, Profile tab
            Verify that clicking courses switcher will open dropdown
            Verify that dropdown has courses and programs options in it
            Verify that clicking each menu will load its screen
        """

        driver = android_login
        global_contents = Globals(setup_logging)
        android_sign_in = AndroidSignIn(driver, setup_logging)

        switcher_label = global_contents.get_element_by_text(driver, 'Courses')
        assert switcher_label
        switcher_label.click()
        course_switcher = android_sign_in.get_all_textviews()[0]
        assert course_switcher.text == 'Courses'
        programs_switcher = android_sign_in.get_all_textviews()[1]
        assert programs_switcher.text == 'Programs'
        course_switcher.click()

        switcher_label = global_contents.get_element_by_text(driver, 'Courses')
        assert switcher_label
        switcher_label.click()
        programs_switcher = android_sign_in.get_all_textviews()[1]
        programs_switcher.click()
        assert global_contents.get_element_by_text(driver, 'Programs')
