"""
    Course Dashboard Test Module
"""

from enums.attributes import ElementAttribute
from framework import expect
from framework.element import Element
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_start_course_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()
        main_dashboard_page = AndroidMainDashboard()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.done_button.click()

        learn_tab = main_dashboard_page.learn_tab
        expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
        expect(learn_tab).to_be_selected()

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
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        course_dashboard_page = AndroidCourseDashboard()

        second_course_name = course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
        assert second_course_name.click()
        if course_dashboard_page.allow_notifications_button:
            assert course_dashboard_page.allow_notifications_button.click()

        expect(course_dashboard_page.course_dashboard_home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)

        videos_tab = course_dashboard_page.course_dashboard_videos_tab
        expect(videos_tab).to_have(values.COURSE_DASHBOARD_VIDEOS_TAB)
        assert videos_tab.click()

        discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
        expect(discussions_tab).to_have(values.COURSE_DASHBOARD_DISCUSSIONS_TAB)
        assert discussions_tab.click()

        dates_tab = course_dashboard_page.course_dashboard_dates_tab
        expect(dates_tab).to_have(values.COURSE_DASHBOARD_DATES_TAB)
        assert dates_tab.click()

        more_tab = course_dashboard_page.course_dashboard_more_tab
        expect(more_tab).to_have(values.COURSE_DASHBOARD_MORE_TAB)
        assert more_tab.click()

        assert course_dashboard_page.back_navigation_button.click()

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

        profile_tab = main_dashboard_page.profile_tab
        assert profile_tab.click()
        assert profile_page.settings_button.click()
        profile_page.privacy_policy_text.scroll_vertically_from_element()
        assert profile_page.profile_txt_logout.click()
        expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)
        profile_page.logout_prompt_logout_button_text.click()
        expect(android_landing.get_search_label).to_have(values.LANDING_SEARCH_TITLE)
