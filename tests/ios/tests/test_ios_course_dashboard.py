"""
    Course Dashboard Screen Test Module
"""
from framework import expect, Element
from tests.common.enums import ElementAttribute
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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f'Starting {TestIosCourseDashboard.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew()
        main_dashboard = IosMainDashboard()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.whats_new_next_button.click()
            setup_logging.info('Whats New screen is successfully loaded')

        learn_tab = main_dashboard.get_main_dashboard_learn_tab
        assert learn_tab.click()
        expect(learn_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        course_dashboard_page = IosCourseDashboard()
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding()

        second_course_name = global_contents.get_element_by_name_ios(set_capabilities, values.MAIN_DASHBOARD_COURSE_NAME)

        second_course_name.click()
        if ios_landing.allow_notifications_button.exists():
            ios_landing.allow_notifications_button.click()

        course_tab = course_dashboard_page.course_dashboard_course_tab
        expect(course_tab).to_have(second_course_name.text)

        videos_tab = course_dashboard_page.course_dashboard_videos_tab
        expect(videos_tab).to_have(values.COURSE_DASHBOARD_VIDEOS_TAB)
        videos_tab.click()

        discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
        expect(discussions_tab).to_have(values.COURSE_DASHBOARD_DISCUSSIONS_TAB)
        assert discussions_tab.click()

        dates_tab = course_dashboard_page.course_dashboard_dates_tab
        expect(dates_tab).to_have(values.COURSE_DASHBOARD_DATES_TAB)
        assert dates_tab.click()

        more_tab = course_dashboard_page.course_dashboard_more_tab
        expect(more_tab).to_have(values.COURSE_DASHBOARD_MORE_TAB)
        assert more_tab.click()

        dashboard_tab = course_dashboard_page.back_navigation_button
        expect(dashboard_tab).to_have(values.LANDING_BACK_BUTTON, ElementAttribute.LABEL)
        assert dashboard_tab.click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

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
