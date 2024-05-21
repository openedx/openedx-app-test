"""
    Main Dashboard Test Module
"""

from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_profile import IosProfile


class TestIosMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard is loaded successfully
        """

        setup_logging.info(f'Starting {TestIosMainDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen,
                Screen Title, Disover Tab
                Profile Tab, Programs Tab, Profiel tab
            Verify that Discover tab will be selected by default
            Verify that clicking each tab will load its screen
        """

        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)
        learn_tab = main_dashboard.get_main_dashboard_learn_tab()
        learn_tab.click()
        assert learn_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        discover_tab = main_dashboard.get_main_dashboard_discover_tab()
        assert discover_tab.text == values.DISCOVER_SCREEN_HEADING
        discover_tab.click()
        assert discover_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

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
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)
        learn_tab = main_dashboard.get_main_dashboard_learn_tab()
        learn_tab.click()
        switcher_label = global_contents.wait_and_get_element(set_capabilities, ios_elements.main_dashboard_dropdown_text)
        assert switcher_label.get_attribute('label') == 'Courses'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'Courses')
        assert switcher_label.get_attribute('label') == 'Courses'
        programs_switcher = global_contents.wait_and_get_element(set_capabilities, 'Programs')
        assert programs_switcher.text == 'Programs'
        course_switcher.click()
        assert switcher_label.get_attribute('label') == 'Courses'
        switcher_label.click()
        programs_switcher.click()
        assert switcher_label.get_attribute('label') == 'Programs'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'Courses')
        course_switcher.click()
        assert switcher_label.get_attribute('label') == 'Courses'
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'settings').click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)

        assert ios_profile.get_profile_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_profile_logout_button().click()
        assert ios_profile.get_logout_close_button().text == 'Close'
        assert ios_profile.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        assert ios_profile.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_logout_button().click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE_IOS
