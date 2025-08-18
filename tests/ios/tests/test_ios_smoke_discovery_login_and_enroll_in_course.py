"""Discovery screen: login from discovery and enroll in course"""

import allure
import pytest

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.course_enrollment_page import CourseEnrollmentPage
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_course_home_tab import IosCourseHomeTab
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew


@allure.epic("DISCOVERY")
@allure.feature("Login and Enrollment")
@allure.story("user can login from discovery page and enroll in course")
@allure.suite("IOS SMOKE")
@pytest.mark.IOS
@pytest.mark.IOS_DISCOVERY
@pytest.mark.IOS_SMOKE
class TestIosDiscoveryLoginAndEnroll:
    """Discovery screen: login from discovery and enroll in course"""

    def test_login_from_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            1. Go to Discover page.
               - Verify discover page is loaded.
            2. Click on Sign in button.
               - Verify sign in page is loaded.
            3. Enter email and password.
            4. Click sign in button.
            5. Dismiss the what's new screen.
               - Verify learn tab is loaded.
            6. Go to profile screen.
               - Verify user is logged in.
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        ios_login = IosLogin()
        ios_landing = IosLanding()
        my_courses_list = IosMyCoursesList()
        main_dashboard_page = IosMainDashboard()
        ios_profile_page = IosProfile()
        whats_new_page = IosWhatsNew()
        ios_discover_page = IosDiscoverPage()

        with allure.step("Verify landing page is loaded successfully"):
            logo_image = ios_landing.edx_logo_image
            expect(logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.explore_all_courses_button).to_have(
                values.LANDING_EXPLORE_COURSES, ElementAttribute.LABEL
            )

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Verify discover screen is loaded successfully"):
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)

        with allure.step("Close AI expert dialogue"):
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.ai_assistant_dismiss_button).not_.to_exist()

        with allure.step("Click on Sign In button"):
            ios_landing.sign_in_button.click()
            expect(ios_login.sign_in_title).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            expect(ios_login.signin_welcome_text).to_have(values.SIGN_IN_MESSAGE, ElementAttribute.LABEL)

        with allure.step("Enter username and password"):
            ios_login.username_textfield.send_keys(global_contents.login_user_name + "\n")
            ios_login.password_textfield.send_keys(global_contents.login_password + "\n")

        with allure.step("Click on Sign In button"):
            ios_login.signin_button.click()
            setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")

        with allure.step("Dismiss the what's new screen if visible"):
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()
            expect(my_courses_list.my_courses_header_text).to_have(
                values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.LABEL
            )

        with allure.step("Go to Profile tab and verify user is logged in"):
            main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            expect(ios_profile_page.full_name_label).to_have(values.PROFILE_NAME_TEXT, ElementAttribute.LABEL)
            expect(ios_profile_page.username_label).to_have(
                f"@{global_contents.login_user_name}", ElementAttribute.LABEL
            )

    def test_enroll_course_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            1. Go to discover page.
            2. Search for course "Demo X".
            3. Click on course "Demo X".
            - Verify edx logo image exists.
            - Verify course name is "edx: DemoX".
            4. Close AI expert dialogue message.
            - Verify start date and end date format.
            - Verify "Advance your career" button.
            5. Click on "Advance your career" button.
            6. Accept allow notification pop-up if it appears.
            - Verify course name.
            - Verify home tab exists.
            - Verify course modules are shown.
            7. Click on back button.
            - "Advance your career" button is greyed out.
            8. Click on back button.
            - Discover result page is loaded.
            9. Open learn tab.
            - "Demo X" course exists under "View All My Courses".
            - Verify course name.
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard = IosMainDashboard()
        ios_discover_page = IosDiscoverPage()
        course_enrollment_page = CourseEnrollmentPage()
        ios_course_home_tab = IosCourseHomeTab()
        course_dashboard_tab = IosCourseDashboard()

        with allure.step("Click on Discover tab"):
            main_dashboard.main_dashboard_discover_tab.click()
            expect(main_dashboard.main_dashboard_discover_tab_selected).to_have(
                values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE
            )
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Search for course Demo X"):
            ios_discover_page.search_field.exists()
            ios_discover_page.search_field.send_keys(values.DEMOX)
            expect(ios_discover_page.search_field).to_have(values.DEMOX, ElementAttribute.VALUE)
            ios_discover_page.search_field.send_keys("\n")
            ios_discover_page.search_button.exists()
            ios_discover_page.search_button.click()
            expect(ios_discover_page.edx_logo_image, timeout=30).to_exist()

        with allure.step("open course demo X"):
            expect(ios_discover_page.demox_course_name).to_exist()
            ios_discover_page.demox_course_name.click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Accept cookies if appear"):
            if course_enrollment_page.accept_cookies_button.exists(raise_exception=False, timeout=30):
                course_enrollment_page.accept_cookies_button.click()

        with allure.step("Close AI expert dialogue"):
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.ai_assistant_dismiss_button).not_.to_exist()

        with allure.step("verify edx logo image and name exists"):
            expect(course_enrollment_page.edx_logo_image).to_exist()
            expect(course_enrollment_page.demo_course_title).to_have(values.DEMOX_COURSE_LABEL, ElementAttribute.LABEL)

        with allure.step("Click on Advance your career button"):
            expect(course_enrollment_page.advance_your_career_button).to_have(
                values.ADCANCE_YOUR_CAREER_LABEL, ElementAttribute.LABEL
            )
            course_enrollment_page.advance_your_career_button.click()

        with allure.step("Accept allow notification if appears"):
            if course_enrollment_page.allow_notifications_button.exists(raise_exception=False):
                course_enrollment_page.allow_notifications_button.click()
                expect(course_enrollment_page.allow_notifications_button).not_.to_exist()

        with allure.step("verify course name and edx org name"):
            ios_course_home_tab.find_by_text_on_screen(values.DEMOX)
            ios_course_home_tab.find_by_text_on_screen(values.MAIN_DASHBOARD_COURSE_ORG)
            expect(course_dashboard_tab.course_dashboard_home_tab).to_exist()

        with allure.step("verify course module are visible"):
            ios_course_home_tab.verify_modules_exists(values.INTRODUCTION_MODULE)
            ios_course_home_tab.verify_modules_exists(values.MODULE_1_EXPERIENCING_COURSE_CONTENT)
            ios_course_home_tab.verify_modules_exists(values.MODULE_2_BEING_SOCIAL)
            ios_course_home_tab.verify_modules_exists(values.MODULE_3_COMPLETING_A_COURSE)
            ios_course_home_tab.verify_modules_exists(values.OPTIONAL_EXAMPLE_PROBLEM_TYPES)
            ios_course_home_tab.verify_modules_exists(values.OPTIONAL_EDX_MOBILE_APP)

        with allure.step("Click on back button to return to course enrollment page"):
            ios_course_home_tab.back_navigation_button.click()
            expect(course_enrollment_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(course_enrollment_page.advance_your_career_button).not_.to_be_enabled()

        with allure.step("Click on back button to return to discover page"):
            course_enrollment_page.enrollment_page_back_button.click()
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.search_field).to_exist()
            expect(ios_discover_page.search_field).to_have(values.DEMOX, ElementAttribute.VALUE)

        with allure.step("open learn tab"):
            main_dashboard.learn_tab.click()
            expect(main_dashboard.course_item_demoX).to_exist()
            main_dashboard.course_item_demoX.get_child_element(main_dashboard.course_name_demoX)
