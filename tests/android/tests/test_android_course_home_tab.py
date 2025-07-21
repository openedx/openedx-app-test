"""
Course Dashboard Home Tab Test Module
"""

import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_home_tab import AndroidCourseHomeTab
from tests.common import values


@pytest.mark.ANDROID
@pytest.mark.ANDROID_SMOKE
class TestAndroidCourseHomeTab:
    """
    Course Dashboard screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
        """
        Scenarios:
            Verify that clicking course from Main dashboard load course dashboard,
            Verify that Course Dashboard tab will show following contents,
            Header contents,
                Back icon,
                Specific "<course name>" as Title, Share icon, Course,
            Verify course deadline title and description
            Verify shift due dates button
            Verify continue with label
            Verify resume button
            Verify introduction section
            Verify subsection element
            Verify clicking subsection element will load component screen
            Verify component header title
            Verify back button
            Verify section element
            Verify second subsection element
            Verify clicking second subsection element will load component screen
            Verify homework element
            Verify second component header
            Verify back button
        """
        course_dashboard_page = AndroidCourseDashboard()

        second_course_name = course_dashboard_page.find_by_text_on_screen(values.MY_COURSES_SECOND_COURSE_NAME)
        expect(second_course_name).to_have(values.MY_COURSES_SECOND_COURSE_NAME)
        assert second_course_name.click()

        if course_dashboard_page.allow_notifications_button:
            assert course_dashboard_page.allow_notifications_button.click()

        expect(course_dashboard_page.course_dashboard_home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_MISSED_DEADLINES_LABEL).exists()

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_DEADLINE_DESCRIPTION_LABEL).exists()

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_SHIFT_DUE_DATES)

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_CONTINUE_WITH_LABEL).exists()

        resume_button = course_dashboard_page.find_by_text_on_screen(values.COURSE_RESUME_BUTTON)
        assert resume_button.exists()
        resume_button.scroll_vertically_from_element()
        introduction_section = course_dashboard_page.find_by_text_on_screen(values.COURSE_SECTION_LABEL)
        assert introduction_section.exists()
        assert introduction_section.click()

        subsection_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_LABEL)
        assert subsection_elem.exists()
        assert subsection_elem.click()

        back_btn = course_dashboard_page.back_button
        assert back_btn.exists()
        assert back_btn.click()
        component_header_title = course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_LABEL)
        component_header_title.scroll_vertically_from_element()

        section1_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_SECTION_1_LABEL)
        assert section1_elem.click()

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_SUBSECTION_1_LABEL).exists()

        homework_elem = course_dashboard_page.find_by_text_on_screen(values.COURSE_COMPONENT_LABEL)
        assert homework_elem.click()

        assert course_dashboard_page.find_by_text_on_screen(values.COURSE_COMPONENT_LABEL).exists()

    def test_component_navigation_smoke(self, android_login, setup_logging):
        """
        Scenarios:
            Verify next button element, and it is clickable
            Verify previous button element, and it is clickable
            Verify user can click on next button until finish button appears
            Verify clicking finish button will load the celebratory modal
            Verify Back to outline button on Modal and clicking this button
                loads the components screen
            Verify clicking on back button will navigate the user to dashboard page
        """

        Element.set_driver(android_login)
        Element.set_logger(setup_logging)
        course_home_page = AndroidCourseHomeTab()

        assert course_home_page.android_loading_circle.wait_to_disappear(90)
        next_btn = course_home_page.next_btn
        expect(next_btn).to_have(values.COURSE_COMPONENT_NEXT_BUTTON)
        assert next_btn.click()

        prev_btn = course_home_page.prev_btn
        expect(prev_btn).to_have(values.COURSE_COMPONENT_PREVIOUS_BUTTON)
        assert prev_btn.click()

        finish_button = course_home_page.component_navigation()
        expect(finish_button).to_have(values.COURSE_COMPONENT_FINISH_BUTTON)
        assert finish_button.click()
        back_to_outline = course_home_page.find_by_text_on_screen(values.COURSE_COMPLETION_BACK_BUTTON)
        assert back_to_outline.exists()
        assert back_to_outline.click()
        back_btn = course_home_page.back_button
        assert back_btn.exists()
        assert back_btn.click()
