"""
    Course Dashboard Screen Test Module
"""

from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import values
from tests.common.globals import Globals


class TestIosCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_start_profile_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Profile is loaded successfully
        """

        setup_logging.info(f'Starting {TestIosCourseDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_next_btn().click()
            setup_logging.info('Whats New screen is successfully loaded')

        learn_tab = main_dashboard.get_main_dashboard_learn_tab()
        learn_tab.click()
        assert learn_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE

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

        course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        second_course = course_dashboard_page.get_my_courses_list()[2]
        assert values.MY_COURSES_SECOND_COURSE_NAME in second_course.text
        second_course.click()

        course_tab = course_dashboard_page.get_course_dashboard_course_tab()
        assert course_tab.text == values.COURSE_DASHBOARD_COURSE_TAB

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

        dashboard_tab = course_dashboard_page.navigate_to_main_dashboard_tab()
        assert dashboard_tab.get_attribute('name') == values.MAIN_DASHBOARD_DASHBOARD_TAB
        dashboard_tab.click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert profile_tab.get_attribute('value') == values.IOS_SELECTED_TAB_VALUE
        assert ios_profile.get_profile_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_profile_logout_button().click()
        assert ios_profile.get_logout_close_button().text == 'Close'
        assert ios_profile.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        assert ios_profile.get_logout_button().text == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_logout_button().click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE_IOS
