"""
Course Dashboard Test Module
"""

import allure
import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.enums import ElementAttribute


@allure.epic("Course Dashboard")
@allure.feature("Dashboard Screen")
@allure.story("User can switch between tabs on course dashboard")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_SMOKE
class TestAndroidCourseDashboard:
    """
    Course Dashboard screen's Test Case
    """

    def test_android_smoke_course_dashboard_screen(self, android_login, setup_logging):
        """
        1 Click on course DemoX
            Allow notifications if popup appears
            verify course dashboard is loaded
            verify back button exist
            verify course name and org is shown

        2 Click on Videos tab
            verify videos tab is loaded

        3 Click on Dates tab
            verify Dates tab is loaded
        4 Click on Discussions tab
            verify Discussions tab is loaded

        5 Click on More tab
            verify More tab is loaded

        6 Click on Back button
            verify learn tab is loaded
        """
        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        course_dashboard_page = AndroidCourseDashboard()
        main_dashboard_page = AndroidMainDashboard()

        with allure.step("Click on course DemoX"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME).click()
            course_dashboard_page.android_loading_circle.wait_to_disappear(30, False)

        with allure.step("Accept notifications if appear"):
            if course_dashboard_page.allow_notifications_button.exists(raise_exception=False):
                course_dashboard_page.allow_notifications_button.click()

        with allure.step("verify course dashboard is loaded"):
            expect(course_dashboard_page.back_button).to_have(
                values.COURSE_DASHBOARD_BACK_BUTTON, ElementAttribute.CONTENT_DESC
            )
            expect(course_dashboard_page.course_dashboard_home_tab).to_exist()

        with allure.step("verify course name and org are shown"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
            course_dashboard_page.find_by_text_on_screen(values.MAIN_DASHBOARD_COURSE_ORG)

        with allure.step("Click on videos tab"):
            expect(course_dashboard_page.course_dashboard_videos_tab).to_exist()
            course_dashboard_page.course_dashboard_videos_tab.click()

        with allure.step("verify videos tab is loaded"):
            expect(course_dashboard_page.video_download_quality_heading).to_exist()
            expect(course_dashboard_page._video_download_to_device_heading).to_exist()

        with allure.step("Click on dates tab"):
            dates_tab = course_dashboard_page.course_dashboard_dates_tab
            expect(dates_tab).to_exist()
            dates_tab.click()

        with allure.step("verify dates tab is loaded"):
            expect(course_dashboard_page.get_text_element_instance(values.DATES_TAB_SYNC_TO_CALENDAR)).to_exist()

        with allure.step("Click on discussions tab"):
            discussions_tab = course_dashboard_page.course_dashboard_discussions_tab
            expect(discussions_tab).to_exist()
            discussions_tab.click()

        with allure.step("verify discussions tab is loaded"):
            expect(course_dashboard_page.get_text_element_instance(values.DISCUSSIONS_SEARCH_BAR)).to_exist()

        with allure.step("Click on more tab"):
            more_tab = course_dashboard_page.course_dashboard_more_tab
            expect(more_tab).to_exist()
            more_tab.click()

        with allure.step("verify more tab is loaded"):
            expect(course_dashboard_page.get_text_element_instance(values.MORE_TAB_HANDOUTS)).to_exist()

        with allure.step("Click on back button"):
            course_dashboard_page.back_button.click()
            expect(main_dashboard_page.learn_tab).to_exist()
