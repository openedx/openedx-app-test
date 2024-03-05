"""
    Main Dashboard Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.globals import Globals


class TestAndroidMainDashboard:
    """
    Main Dashboard screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidMainDashboard.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_signin_button()
        assert android_landing.load_signin_screen().text == values.LOGIN

        assert android_sign_in.get_sign_in_email_label().text == values.EMAIL_OR_USERNAME
        email_field = android_sign_in.get_sign_in_tf_email()
        assert email_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        email_field.send_keys(global_contents.login_user_name)

        assert android_sign_in.get_sign_in_password_label().text == values.PASSWORD
        password_field = android_sign_in.get_sign_in_password_field()
        assert password_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        password_field.send_keys(global_contents.login_password)
        assert android_sign_in.get_signin_button().get_attribute('clickable') == values.TRUE_LOWERCASE
        android_sign_in.get_signin_button().click()

        if global_contents.whats_new_enable:
            close_btn = whats_new_page.get_close_button()
            close_btn.click()

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
        discover_tab = main_dashboard_page.get_discover_tab()
        assert discover_tab.get_attribute('content-desc') == values.DISCOVER_SCREEN_HEADING
        assert discover_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        dashboard_tab = main_dashboard_page.get_dashboard_tab()
        assert dashboard_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_DASHBOARD_TAB
        dashboard_tab.click()
        assert dashboard_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        programs_tab = main_dashboard_page.get_programs_tab()
        assert programs_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROGRAMS_TAB
        programs_tab.click()
        assert programs_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        profile_tab = main_dashboard_page.get_profile_tab()
        assert profile_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('selected') == values.TRUE_LOWERCASE
