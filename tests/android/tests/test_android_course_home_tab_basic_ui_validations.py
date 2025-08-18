"""
Course Dashboard Home Tab Test Module
"""

import allure
import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_home_tab import AndroidCourseHomeTab
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.enums.attributes import ElementAttribute


@allure.epic("Course Dashboard")
@allure.feature("Home Tab")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_SMOKE
class TestAndroidCourseHomeTabBasicUiValidation:
    """
    Course Dashboard screen's Test Case: basic ui validation
    """

    def test_android_course_home_tab_validate_ui_elements(self, android_login, setup_logging):
        """
        Steps:
        1. Click on course “DemoX”
        2. Verify that Course Dashboard shows the following contents:
            - Header contents:
            - Back button
            - Specific "<course name>" as Title
            - Home tab is shown as selected
            - Missed deadline title: “Missed some deadlines?“
            - Description:
                “Don't worry - shift our suggested schedule to complete past due
                assignments without losing any progress.“
            - Shift due dates button
            - Continue with label
            - Resume button
            - Assignment progress bar with description: “0 of 3 assignments complete”
            - All modules exist on screen:
            - Introduction
            - Module 1: Experiencing Course Content (download icon exists)
            - Module 2: Being Social (download icon exists)
            - Module 3: Completing a Course (download icon exists)
            - Optional: Example Problem Types
            - Optional: edX Mobile App (download icon exists)
        """

        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        course_dashboard_page = AndroidCourseDashboard()
        course_home_tab = AndroidCourseHomeTab()
        main_dashboard_page = AndroidMainDashboard()

        with allure.step("click on course DemoX"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME).click()
            course_dashboard_page.android_loading_circle.wait_to_disappear(30, False)

        with allure.step("verify header contents"):
            if course_home_tab.allow_notifications_button.exists(raise_exception=False):
                course_home_tab.allow_notifications_button.click()
            expect(course_dashboard_page.back_button).to_have(
                values.COURSE_DASHBOARD_BACK_BUTTON, ElementAttribute.CONTENT_DESC
            )
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
            course_dashboard_page.find_by_text_on_screen(values.MAIN_DASHBOARD_COURSE_ORG)
            expect(course_dashboard_page.course_dashboard_home_tab).to_exist()

        with allure.step("verify missed deadline title and description"):
            course_home_tab.find_by_text_on_screen(values.COURSE_MISSED_DEADLINES_LABEL)
            course_home_tab.find_by_text_on_screen(values.COURSE_DEADLINE_DESCRIPTION_LABEL)
            expect(course_home_tab.find_by_text_on_screen(values.COURSE_SHIFT_DUE_DATES)).to_be_enabled()
            expect(course_home_tab.close_missed_deadline_msg_button).to_have(
                values.COURSE_MISSED_DEADLINE_MSG_CANCEL_BUTTON, ElementAttribute.CONTENT_DESC
            )

        with allure.step("verify continue with label and resume button"):
            course_home_tab.find_by_text_on_screen(values.COURSE_CONTINUE_WITH_LABEL)
            expect(course_home_tab.find_by_text_on_screen(values.COURSE_RESUME_BUTTON)).to_be_enabled()

        with allure.step("verify assignment progress bar"):
            expect(course_home_tab.android_progress_bar).to_have(values.COURSE_ASSIGNMENT_PROGRESSBAR_VALUE)
            course_home_tab.find_by_text_on_screen(values.COURSE_ASSIGNMENT_PROGRESS_DESCRIPTION)

        with allure.step("verify all modules exist on screen"):
            course_home_tab.verify_modules_exists(values.INTRODUCTION_MODULE)
            course_home_tab.verify_modules_exists(values.MODULE_1_EXPERIENCING_COURSE_CONTENT)
            course_home_tab.verify_modules_exists(values.MODULE_2_BEING_SOCIAL)
            course_home_tab.verify_modules_exists(values.MODULE_3_COMPLETING_A_COURSE)
            course_home_tab.verify_modules_exists(values.OPTIONAL_EXAMPLE_PROBLEM_TYPES)
            course_home_tab.verify_modules_exists(values.OPTIONAL_EDX_MOBILE_APP)

        with allure.step("click on back button to navigate to main dashboard page"):
            course_dashboard_page.back_button.click()
            expect(main_dashboard_page.learn_tab).to_exist()
