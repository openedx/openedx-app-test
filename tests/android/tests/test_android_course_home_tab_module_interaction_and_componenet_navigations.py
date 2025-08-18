"""
Course Dashboard Home Tab Test Module
"""

import allure
import pytest

from framework import expect, Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_home_tab import AndroidCourseHomeTab
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.common import values
from tests.common.enums import ElementAttribute


@allure.epic("Course Dashboard")
@allure.feature("Home Tab")
@allure.story("User can ")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_SMOKE
class TestAndroidCourseHomeTabSectionsAndComponents:
    """Course Dashboard Screen's Test: course modules interaction and component navigation"""

    def test_android_smoke_course_home_tab_sections_and_component_navigation(self, android_login, setup_logging):
        """
        1. Go to Course Home tab screen

        2. Open Introduction section dropdown
           - Verify subsection element “Welcome to an edX Course!” exists

        3. Click on download icon on introduction section
           - Verify downloading starts
           - Verify downloading is complete

        4. Click on the remove downloaded course section icon
           - Popup message is displayed with title “Warning”
                and description “Are you sure you want to delete video(s) for ‘Introduction’?”
           - Verify “Cancel” and “Delete” buttons exist

        5. Click on Cancel button
           - Verify popup is closed

        6. Click on the remove downloaded icon again and click on Delete button
           - Verify download icon is now shown

        7. Click subsection element
           - Verify clicking subsection element loads component screen
           - Verify component header title
           - Verify Next button exists
           - Verify Back button exists

        8. Click on Back button
           - Verify second section element “Module 1: Experiencing Course Content” exists

        9. Click on Second section element
           - Verify subsections are shown
           - Verify homework element exists

        10. Click on subsection Lesson 1
            - Verify section header and Next button

        11. Click on Next button
            - New screen is loaded
            - Verify “Prev” button

        12. Click on Prev button
            - First screen is loaded again

        13. Click on Next button until Finish button is reached

        14. Click on Finish button
            - Verify celebratory modal appears with title “Good job!”
                and description “You’ve completed ‘Getting Around’.”
            - Verify buttons Next section and Back to outline exist
            - Verify “x” close button exists

        15. Click on Close button
            - Verify Finish button is shown

        17. Click on Finish button
            - Verify celebratory modal is loaded

        18. Click on Back to outline button
            - Verify Home tab is loaded with sections displayed

        19. Click on Homework1
            - Verify Homework 1 course content is loaded with Next button displayed

        20. Click on Next button
            - Verify Problem 1 is loaded with question: “In which country is the edX main office located?”

        21. Enter an answer and click on Next button
            - New problem is loaded

        22. Click on Back navigation button
            - Home tab is loaded

        23. Click on Back button
            - Learn tab is loaded
        """
        driver = android_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        course_home_tab = AndroidCourseHomeTab()
        course_dashboard_page = AndroidCourseDashboard()
        main_dashboard_page = AndroidMainDashboard()

        with allure.step("Go to course home tab"):
            course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME).click()
            course_dashboard_page.android_loading_circle.wait_to_disappear(30, False)

        with allure.step("Open Introduction section dropdown"):
            if course_home_tab.allow_notifications_button.exists(raise_exception=False):
                course_home_tab.allow_notifications_button.click()
            course_home_tab.find_by_text_on_screen(values.INTRODUCTION_MODULE)
            if not course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL, False).exists(
                raise_exception=False
            ):
                course_home_tab.find_by_text_on_screen(values.INTRODUCTION_MODULE).click()
            course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)

        with allure.step("Click on download icon on introduction section"):
            course_home_tab.download_course_section_button.click()
            course_home_tab.stop_download_course_section_button.wait_to_disappear(20)
            expect(course_home_tab.remove_downloaded_course_section_button).to_exist()

        with allure.step("click on remove downloaded course section button"):
            course_home_tab.remove_downloaded_course_section_button.click()
            course_home_tab.find_by_text_on_screen(values.REMOVE_DOWNLOADED_COURSE_SECTION_WARNING_TITLE)
            course_home_tab.find_by_text_on_screen(values.REMOVE_DOWNLOADED_COURSE_SECTION_WARNING_DELETE_BUTTON)

        with allure.step("click on cancel button on remove downloaded course section warning"):
            course_home_tab.find_by_text_on_screen(
                values.REMOVE_DOWNLOADED_COURSE_SECTION_WARNING_CANCEL_BUTTON
            ).click()
            expect(
                course_home_tab.get_text_element_instance(values.REMOVE_DOWNLOADED_COURSE_SECTION_WARNING_TITLE)
            ).not_.to_exist()

        with allure.step("click on remove downloaded course section button again"):
            course_home_tab.remove_downloaded_course_section_button.click()

        with allure.step("Click on delete download button"):
            course_home_tab.find_by_text_on_screen(
                values.REMOVE_DOWNLOADED_COURSE_SECTION_WARNING_DELETE_BUTTON
            ).click()
            expect(course_home_tab.download_course_section_button).to_exist()

        with allure.step("Click on sub section element of introduction module"):
            course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL).click()
            course_home_tab.android_loading_circle.wait_to_disappear(30)
            course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)
            course_home_tab.find_by_text_on_screen(values.COURSE_COMPONEMT_FIRST_CONTENT_HEADING)

        with allure.step("Verify back and next button on course component screen"):
            expect(course_home_tab.back_button).to_exist()
            expect(course_home_tab.next_btn).to_exist()

        with allure.step("Click on back button to navigate to course home tab"):
            course_home_tab.back_button.click()
            course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)

        with allure.step("Click on Module 1: Experiencing Course Content section"):
            course_home_tab.find_by_text_on_screen(values.MODULE_1_EXPERIENCING_COURSE_CONTENT).click()
            Element.swipe_vertical_full_page()
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_1_LABEL)
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_HOMEWORK1_LABEL)

        with allure.step("Open subsection Lesson 1: edX Content Basics"):
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_1_LABEL).click()
            course_home_tab.android_loading_circle.wait_to_disappear(30)
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_1_LABEL)
            course_home_tab.find_by_text_on_screen(values.COURSE_COMPONENT_SCREEN1_LABEL)

        with allure.step("verify next button is enabled and click on it"):
            next_button = course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.next_btn)
            expect(next_button).to_be_enabled()
            next_button.long_press()
            course_home_tab.android_loading_circle.wait_to_disappear(30)

        with allure.step("verify previous button is enabled"):
            prev_btn = course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.prev_btn)
            expect(prev_btn).to_be_enabled()
            course_home_tab.find_by_text_on_screen(values.COURSE_COMPONENT_SCREEN1_LABEL)

        with allure.step("click on previous button"):
            prev_btn = course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.prev_btn)
            prev_btn.click()
            course_home_tab.android_loading_circle.wait_to_disappear(30)
            expect(
                course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.prev_btn, False)
            ).not_.to_exist()

        with allure.step("click next button until finish button appears"):
            finish_button = course_home_tab.navigate_components_until_last_screen_is_reached()
            finish_button.click()

        with allure.step("verify celebratory modal appears"):
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_TITLE)
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_DESCRIPTION)
            expect(course_home_tab.close_missed_deadline_msg_button).to_have(
                values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_CLOSE_BUTTON, ElementAttribute.CONTENT_DESC
            )
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_NEXT_BUTTON)
            course_home_tab.find_by_text_on_screen(
                values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_BACK_TO_OUTLINE_BUTTON
            )

        with allure.step("click on close button on celebratory modal"):
            course_home_tab.close_missed_deadline_msg_button.click()
            course_home_tab.android_loading_circle.wait_to_disappear(20)
            expect(
                course_home_tab.get_text_element_instance(values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_TITLE)
            ).not_.to_exist()

        with allure.step("click on Finish button again"):
            course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.finish_button).click()
            course_home_tab.android_loading_circle.wait_to_disappear(20)
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_TITLE)

        with allure.step("Click on back to outline button on celebratory modal"):
            course_home_tab.get_text_element_instance(
                values.COURSE_SUBSECTION_COMPLETION_CELEBRATORY_MODAL_BACK_TO_OUTLINE_BUTTON
            ).click()
            course_home_tab.android_loading_circle.wait_to_disappear(10, raise_exception=False)
            course_home_tab.find_by_text_on_screen(values.COURSE_INTRO_MODULE_SUBSECTION_LABEL)

        with allure.step("verify course home tab is loaded"):
            expect(course_dashboard_page.course_dashboard_home_tab).to_exist()

        with allure.step("navigate to homework 1 sub section"):
            homework1_sub_section = course_home_tab.get_text_element_instance(
                values.COURSE_SUBSECTION_HOMEWORK1_LABEL
            ).scroll_and_find()
            homework1_sub_section.click()
            course_home_tab.android_loading_circle.wait_to_disappear(20)
            course_home_tab.find_by_text_on_screen(values.COURSE_SUBSECTION_HOMEWORK1_LABEL)

        with allure.step("click on next button"):
            next_button = course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.next_btn)
            next_button.click()
            course_home_tab.android_loading_circle.wait_to_disappear(20)
            course_home_tab.course_component_bottom_nav_bar.get_child_element(course_home_tab.prev_btn)

        with allure.step("enter answer and verify"):
            course_home_tab.edit_text_view.send_keys("Test answer")
            expect(course_home_tab.edit_text_view).to_have("Test answer")

        with allure.step("click on back button to navigate to course dashboard page"):
            back_btn = course_home_tab.back_button
            expect(back_btn).to_exist()
            back_btn.click()
            expect(course_dashboard_page.course_dashboard_home_tab).to_exist()

        with allure.step("click on back button to navigate to main dashboard page"):
            course_dashboard_page.back_button.click()
            expect(main_dashboard_page.learn_tab).to_exist()
