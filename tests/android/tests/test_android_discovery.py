"""
    Discovery Test Module
"""

from time import *
from tests.common import values
from tests.common.globals import Globals
from tests.android.pages import android_elements
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from appium.webdriver.common.mobileby import MobileBy
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard


class TestAndroidDiscovery:
    """
    Discovery screen's Test Case
    """

    def test_start_discovery_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discovery screen is loaded successfully
            Verify that the screen title is correct
            Verify that the explore courses button is displayed
            Verify that the explore courses button text is correct
            Verify that the back button is displayed
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
        """

        setup_logging.info(f'Starting {TestAndroidDiscovery.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_explore_courses().text == values.LANDING_EXLPORE_COURSES
        android_landing.get_explore_courses().click()

        back_button = global_contents.get_back_button(set_capabilities)
        assert back_button.get_attribute('displayed') == values.TRUE_LOWERCASE
        assert global_contents.get_txt_toolbar_title(set_capabilities).text == values.DISCOVERY_SCREEN_TITLE

        discovery_message = global_contents.get_android_element_by_text(set_capabilities, values.DISCOVERY_SCREEN_MESSAGE)
        assert discovery_message.text == values.DISCOVERY_SCREEN_MESSAGE

    def test_discovery_search_and_trending(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify search field is displayed
            Verify search field hint text
            Verify search button is displayed
            Verify search button text
            Verify trending label is displayed
            Verify trending label text
            Verify python course is displayed
            Verify python course text
            Verify excel course is displayed
            Verify excel course text
            Verify data course is displayed
            Verify data course text
            Verify marketing course is displayed
            Verify marketing course text
        """

        global_contents = Globals(setup_logging)

        search_field = global_contents.wait_and_get_element(set_capabilities, android_elements.discovery_search_field)
        assert search_field.get_attribute('hint') == values.DISCOVERY_SEARCH_FIELD

        search_button = global_contents.wait_and_get_element(set_capabilities, android_elements.discovery_search_button)
        assert search_button.text == values.DISCOVERY_SEARCH_BUTTON

        trending_label = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_TRENDING_LABEL)
        assert trending_label.text == values.DISCOVERY_TRENDING_LABEL

        python_label = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_TRENDING_COURSE_PYTHON)
        assert python_label.text == values.DISCOVERY_TRENDING_COURSE_PYTHON

        excel_label = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_TRENDING_COURSE_EXCEL)
        assert excel_label.text == values.DISCOVERY_TRENDING_COURSE_EXCEL

        data_label = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_TRENDING_COURSE_DATA)
        assert data_label.text == values.DISCOVERY_TRENDING_COURSE_DATA

        marketing_label = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_TRENDING_COURSE_MARKETING)
        assert marketing_label.text == values.DISCOVERY_TRENDING_COURSE_MARKETING

    def test_discovery_popular_subjects(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify main content is displayed
            Verify main content text
            Verify search breadcrumb is displayed
            Verify search breadcrumb text
            Verify filter by popular courses is displayed
            Verify filter by popular courses text
            Verify first popular course is displayed
            Verify first popular course text
            Verify second popular course is displayed
            Verify second popular course text
            Verify third popular course is displayed
            Verify third popular course text
            Verify third popular course is clicked
            Verify results number is displayed
            Verify results number text
            Verify show results number is displayed
            Verify show results number text
            Verify show results number is clicked
            Verify pagination results is displayed
            Verify pagination results text
            Verify pagination text is displayed
        """

        global_contents = Globals(setup_logging)
        main_content = global_contents.wait_and_get_element(set_capabilities, android_elements.discovery_main_content)
        assert main_content.text == values.DISCOVERY_MAIN_CONTENT

        bread_crum = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_SEARCH_BREADCRUMB)
        assert bread_crum.text == values.DISCOVERY_SEARCH_BREADCRUMB

        popular_courses = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_FILTER_BY_POPULAR_COURSES)
        assert popular_courses.text == values.DISCOVERY_FILTER_BY_POPULAR_COURSES

        discovery_message = global_contents.get_android_element_by_text(set_capabilities, values.DISCOVERY_SCREEN_MESSAGE)
        assert discovery_message.text == values.DISCOVERY_SCREEN_MESSAGE

        global_contents.scroll_screen(set_capabilities, popular_courses, discovery_message)

        first_popular_course = global_contents.wait_and_get_element(set_capabilities, android_elements.Discovery_first_popular_course)
        assert first_popular_course.get_attribute('content-desc') == values.DISCOVERY_FIRST_POPULAR_COURSE

        second_popular_course = global_contents.wait_and_get_element(set_capabilities, android_elements.Discovery_second_popular_course)
        assert second_popular_course.get_attribute('content-desc') == values.DISCOVERY_SECOND_POPULAR_COURSE

        global_contents.scroll_screen(set_capabilities, second_popular_course, first_popular_course)

        math_course = global_contents.wait_and_get_element(set_capabilities, android_elements.Discovery_third_popular_course)
        assert math_course.get_attribute('content-desc') == values.DISCOVERY_POPULAR_MATH_COURSE
        math_course.click()
        sleep(10)
        results_number = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_MATH_RESULTS)
        assert results_number.text == values.DISCOVERY_MATH_RESULTS
        sleep(5)
        show_results_number = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_MATH_RESULTS_BUTTON)
        assert show_results_number.text == values.DISCOVERY_MATH_RESULTS_BUTTON
        show_results_number.click()
        pagination_results = global_contents.get_element_by_exact_text_android(set_capabilities, values.DISCOVERY_MATH_PAGINATION_RESULTS)
        assert pagination_results.text == values.DISCOVERY_MATH_PAGINATION_RESULTS
        pagination_text = global_contents.get_element_by_exact_text_android(
            set_capabilities, values.DISCOVERY_PAGINATION_TEXT)
        assert pagination_text.text == values.DISCOVERY_PAGINATION_TEXT

    def test_login_from_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the user is able to login from discovery screen
            Verify that the user is able to navigate to the discover tab
        """

        global_contents = Globals(setup_logging)
        android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

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
            whats_new_page.get_close_button().click()
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')

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

        global_contents = Globals(setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discover_tab = main_dashboard_page.get_discover_tab()
        assert discover_tab.get_attribute('content-desc') == values.DISCOVER_SCREEN_HEADING
        assert discover_tab.get_attribute('selected') == values.FALSE_LOWERCASE
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == values.TRUE_LOWERCASE

        assert global_contents.get_txt_toolbar_title(set_capabilities).text == values.DISCOVERY_SCREEN_TITLE
        discovery_message = global_contents.get_android_element_by_text(
            set_capabilities, values.DISCOVERY_SCREEN_MESSAGE)
        assert discovery_message.text == values.DISCOVERY_SCREEN_MESSAGE
        discovery_message.click()
        marketing_label = global_contents.get_element_by_exact_text_android(
            set_capabilities, values.DISCOVERY_TRENDING_COURSE_MARKETING)
        assert marketing_label.text == values.DISCOVERY_TRENDING_COURSE_MARKETING

        global_contents.scroll_screen(set_capabilities, marketing_label, discovery_message)

        global_contents.wait_for_element_visibility(set_capabilities, android_elements.discovery_search_field)
        search_field = global_contents.get_all_views_on_screen(set_capabilities, 'android.widget.EditText')[0]
        assert search_field.get_attribute('displayed') == 'true'
        assert search_field.get_attribute('clickable') == 'true'
        assert search_field.get_attribute('hint') == values.DISCOVERY_SEARCH_FIELD
        search_field.click()
        search_field.send_keys('Demo X')

        sleep(10)
        result = global_contents.wait_and_get_element(set_capabilities, android_elements.discovery_first_search_result)
        assert result.text == values.DISCOVERY_DEMOX_COURSE
        result.click()

    def test_search_course_in_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the enrollment page is loaded successfully
            Verify that the enrollment date is displayed
            Verify that the enrollment date is clickable
            Verify that the enroll button is displayed
            Verify that the enroll button text is correct
            Verify that the enroll button is clickable
            Verify that the allow notifications button is displayed
            Verify that the allow notifications button text is correct
            Verify that the allow notifications button is clickable
            Verify that the home tab is displayed
            Verify that the home tab text is correct
        """

        course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        enroll_main_element = set_capabilities.find_element_by_xpath(android_elements.discovery_enroll_main_element)
        enrollment_date = enroll_main_element.find_element_by_class_name(android_elements.all_textviews)
        assert enrollment_date.text
        enrollment_date.click()

        enroll_button = set_capabilities.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                      f'new UiSelector().description("Enroll")')
        assert enroll_button.get_attribute('content-desc') == 'Enroll'
        enroll_button.click()

        if course_dashboard_page.get_allow_notifications_button():
            course_dashboard_page.get_allow_notifications_button().click()

        home_tab = course_dashboard_page.get_course_dashboard_home_tab()
        assert home_tab.text == values.COURSE_DASHBOARD_HOME_TAB
