"""
    Main Dashboard Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_landing import IosLanding
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f'Starting {TestIosMainDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            whats_new_page.whats_new_next_button.click()
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard = IosMainDashboard()
        learn_tab = main_dashboard.get_main_dashboard_learn_tab
        assert learn_tab.click()
        expect(learn_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

        discover_tab = main_dashboard.main_dashboard_discover_tab
        assert discover_tab.click()
        expect(discover_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

        profile_tab = main_dashboard.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB)
        assert profile_tab.click()

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        main_dashboard = IosMainDashboard()
        learn_tab = main_dashboard.get_main_dashboard_learn_tab
        assert learn_tab.click()
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
        programs_switcher = global_contents.wait_and_get_element(set_capabilities, 'Programs')
        programs_switcher.click()
        assert switcher_label.get_attribute('label') == 'Programs'
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(set_capabilities, 'Courses')
        course_switcher.click()
        assert switcher_label.get_attribute('label') == 'Courses'

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
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
