"""
    Main Dashboard Test Module
"""

from enums.attributes import ElementAttribute
from framework import expect
from framework.element import Element
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features).to_have('Done')
            assert whats_new_page.done_button.click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
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
        main_dashboard_page = AndroidMainDashboard()

        learn_tab = main_dashboard_page.learn_tab
        expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
        expect(learn_tab).to_be_selected()

        discover_tab = main_dashboard_page.discover_tab
        expect(discover_tab).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.CONTENT_DESC)
        expect(discover_tab).to_not.to_be_selected()
        assert discover_tab.click()
        expect(discover_tab).to_be_selected()

        profile_tab = main_dashboard_page.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.CONTENT_DESC)
        expect(profile_tab).to_not.to_be_selected()
        assert profile_tab.click()
        expect(profile_tab).to_be_selected()
        assert main_dashboard_page.learn_tab.click()

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
        android_sign_in = AndroidSignIn()
        main_dashboard = AndroidMainDashboard()

        
        assert main_dashboard.switcher_label_courses.exists()
        assert main_dashboard.switcher_label_courses.click()
        text_views = android_sign_in.text_view.find_all()
        expect(text_views[0]).to_have('Courses')
        expect(text_views[1]).to_have('Programs')
        assert text_views[0].click()
        assert main_dashboard.switcher_label_courses.exists()
        assert main_dashboard.switcher_label_courses.click()
        text_views = android_sign_in.text_view.find_all()
        assert text_views[1].click()
        assert main_dashboard.switcher_label_programs.exists()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        profile_page = AndroidProfile()
        android_landing = AndroidLanding()
        main_dashboard_page = AndroidMainDashboard()

        assert main_dashboard_page.profile_tab.click()
        assert profile_page.settings_button.click()
        profile_page.privacy_policy_text.scroll_vertically_from_element()
        assert profile_page.profile_txt_logout.click()
        expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)
        assert profile_page.logout_prompt_logout_button_text.click()
        expect(android_landing.get_search_label).to_have(values.LANDING_SEARCH_TITLE)
