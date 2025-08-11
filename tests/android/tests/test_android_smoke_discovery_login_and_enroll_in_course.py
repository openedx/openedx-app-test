"""Module Discovery login and enroll functionality"""

import allure
import pytest

from framework import expect, Element
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals


@allure.epic("DISCOVERY")
@allure.feature("Login and Enrollment")
@allure.story("user can login from discovery page and enroll in course")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_DISCOVERY
@pytest.mark.ANDROID_SMOKE
class TestAndroidDiscoveryLoginAndEnroll:
    """
    Discovery screen: search and trending tags
    """

    def test_login_from_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the user is able to log in from discovery screen
            Verify that the user is able to navigate to the discover tab
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        catalog_page = AndroidCatalogPage()
        android_sign_in = AndroidSignIn()
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()
        main_dashboard_page = AndroidMainDashboard()
        course_dashboard_page = AndroidCourseDashboard()

        with allure.step("Goto Discover page"):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            expect(android_landing.explore_all_courses_button).to_have(values.LANDING_EXPLORE_COURSES)
            android_landing.explore_all_courses_button.click()
            expect(android_landing.back_navigation_button).to_be_displayed()
            expect(catalog_page.catalog_screen_heading_msg, timeout=30).to_exist()

        assert android_landing.signin_button.exists()
        assert android_landing.load_signin_screen()
        expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.SIGN_IN_TEXT)

        expect(android_sign_in.sign_in_email_label).to_have(values.EMAIL_OR_USERNAME)
        expect(android_sign_in.sign_in_tf_email).to_be_clickable()
        assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)

        expect(android_sign_in.sign_in_password_label).to_have(values.PASSWORD)
        expect(android_sign_in.sign_in_password_field).to_be_clickable()
        assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)
        expect(android_sign_in.signin_button).to_be_clickable()
        assert android_sign_in.signin_button.click()
        setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")
        if whats_new_page.get_close_button.exists(timeout=20, raise_exception=False):
            assert whats_new_page.get_close_button.click()
        learn_tab = main_dashboard_page.learn_tab
        expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
        expect(learn_tab).to_be_selected()

        assert course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)

    def test_enroll_course_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discover tab is loaded successfully
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
            Verify that the search field is displayed
            Verify that the search field hint text is correct
            Verify that the search field is clickable
            Verify that the search field is filled with text
            Verify that the search result is displayed
            Verify that the search result text is correct
            Verify that the search result is clickable
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        catalog_page = AndroidCatalogPage()
        course_dashboard = AndroidCourseDashboard()

        discover_tab = main_dashboard_page.discover_tab
        expect(discover_tab).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.CONTENT_DESC)
        expect(discover_tab).not_.to_be_selected()
        assert discover_tab.click()
        expect(discover_tab).to_be_selected()

        expect(catalog_page.text_toolbar_title).to_have(values.DISCOVERY_SCREEN_TITLE)
        expect(catalog_page.catalog_screen_heading_msg, timeout=30).to_exist()

        search_field = catalog_page.search_field
        expect(search_field).to_be_displayed()
        expect(search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, "hint")
        if catalog_page.ai_assistant_dismiss_button.exists(raise_exception=False, timeout=30):
            catalog_page.ai_assistant_dismiss_button.click()
        search_field.click()
        assert search_field.send_keys("Demo X")
        catalog_page.search_button.exists()
        assert catalog_page.search_button.click()
        expect(catalog_page.demox_course_logo_desc).to_exist()
        assert catalog_page.demox_course_logo_desc.click()
        assert catalog_page.find_by_text_on_screen("edX: DemoX")

        catalog_page.android_loading_circle.wait_to_disappear()

        with allure.step("Accept cookies if popup appears"):
            if catalog_page.accept_cookies_button.exists(raise_exception=False, timeout=30):
                catalog_page.accept_cookies_button.click()
        with allure.step("dismiss ai chat popup appears"):
            if catalog_page.ai_assistant_dismiss_button.exists(raise_exception=False, timeout=20):
                catalog_page.ai_assistant_dismiss_button.click()

        enroll_main_element = catalog_page.discovery_enroll_main_element
        enrollment_date = enroll_main_element.get_child_element(catalog_page.course_start_date)
        expect(enrollment_date).to_match(r".+")
        advance_your_career_button = enroll_main_element.get_child_element(catalog_page.advance_your_career_button)
        advance_your_career_button.click()
        if catalog_page.advance_your_career_button.exists(raise_exception=False):
            enroll_main_element.get_child_element(catalog_page.advance_your_career_button).click()
        if catalog_page.allow_notifications_button.exists(raise_exception=False):
            catalog_page.allow_notifications_button.click()
        expect(course_dashboard.course_dashboard_home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)
        course_dashboard.back_button.click()
        course_dashboard.android_loading_circle.wait_to_disappear()
        course_dashboard.back_button.click()
