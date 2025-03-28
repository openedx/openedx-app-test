"""
    Course Home Tab Screen Test Module
"""

from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages import ios_elements
from tests.common import values
from tests.common.globals import Globals
from tests.ios.pages.ios_course_home_tab import IosCourseHomeTab


class TestIosCourseHomeTab:
    """
    Course Home Tab screen's Test Case
    """

    def test_validate_ui_elements(self, ios_login, setup_logging):
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
        driver = ios_login
        course_dashboard_page = IosCourseDashboard(driver, setup_logging)
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding(driver, setup_logging)

        second_course_name = global_contents.get_element_by_name_ios(
            driver, values.MY_COURSES_SECOND_COURSE_NAME)

        second_course_name.click()
        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()

        course_tab = course_dashboard_page.get_course_dashboard_course_tab()
        assert course_tab.text == values.COURSE_DASHBOARD_HOME_TAB

        deadline_title = global_contents.get_element_by_label_ios(
            driver, values.COURSE_MISSED_DEADLINES_LABEL)
        assert deadline_title.text == values.COURSE_MISSED_DEADLINES_LABEL

        deadline_description = global_contents.get_element_by_label_ios(
            driver, values.COURSE_DEADLINE_DESCRIPTION_LABEL)
        assert deadline_description.text == values.COURSE_DEADLINE_DESCRIPTION_LABEL

        shift_due_dates_button = global_contents.get_element_by_label_ios(
            driver, values.COURSE_SHIFT_DUE_DATES)
        assert shift_due_dates_button.text == values.COURSE_SHIFT_DUE_DATES

        continue_with_lable = global_contents.get_element_by_label_ios(
            driver, values.COURSE_RESUME_WITH_LABEL)
        assert continue_with_lable.text == values.COURSE_RESUME_WITH_LABEL

        resume_button = global_contents.get_elements_by_name_ios(driver, values.COURSE_RESUME_BUTTON)[1]
        assert resume_button.text == values.COURSE_RESUME_BUTTON

        global_contents.scroll_from_element(driver, resume_button)
        introduction_section = global_contents.get_element_by_label_ios(driver, values.COURSE_SECTION_LABEL)
        assert introduction_section.text == values.COURSE_SECTION_LABEL
        introduction_section.click()

        subsection_elem = global_contents.get_element_by_label_ios(driver, values.COURSE_SUBSECTION_LABEL)
        assert subsection_elem.text == values.COURSE_SUBSECTION_LABEL
        subsection_elem.click()

        component_header_title = global_contents.get_element_by_label_ios(
            driver, values.COURSE_SUBSECTION_LABEL)
        assert component_header_title.text == values.COURSE_SUBSECTION_LABEL

        back_btn = global_contents.wait_and_get_element(driver, ios_elements.course_dashboard_back_button)
        assert back_btn.text == values.LANDING_BACK_BUTTON
        back_btn.click()

        section1_elem = global_contents.get_element_by_label_ios(driver, values.COURSE_SECTION_1_LABEL)
        assert section1_elem.text == values.COURSE_SECTION_1_LABEL
        section1_elem.click()

        subsection1_elem = global_contents.get_element_by_label_ios(driver, values.COURSE_SUBSECTION_1_LABEL)
        assert subsection1_elem.text == values.COURSE_SUBSECTION_1_LABEL

        homework_elem = global_contents.get_element_by_label_ios(driver, values.COURSE_COMPONENT_LABEL)
        assert homework_elem.text == values.COURSE_COMPONENT_LABEL
        homework_elem.click()

        component_header = global_contents.get_element_by_label_ios(driver, values.COURSE_COMPONENT_LABEL)
        assert component_header.text == values.COURSE_COMPONENT_LABEL

    def test_component_navigation_smoke(self, set_capabilities, setup_logging):
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

        global_contents = Globals(setup_logging)
        course_home_page = IosCourseHomeTab(set_capabilities, setup_logging)

        next_btn = course_home_page.get_next_btn()
        assert next_btn.text == values.COURSE_COMPONENT_NEXT_BUTTON
        next_btn.click()

        prev_btn = course_home_page.get_prev_btn()
        assert prev_btn.text == values.COURSE_COMPONENT_PREVIOUS_BUTTON
        prev_btn.click()

        finish_button = course_home_page.component_navigation()
        assert finish_button.text == values.COURSE_COMPONENT_FINISH_BUTTON
        finish_button.click()

        back_to_outline = global_contents.get_element_by_label_ios(
            set_capabilities, values.COURSE_COMPLETION_BACK_BUTTON)
        assert back_to_outline.text == values.COURSE_COMPLETION_BACK_BUTTON
        back_to_outline.click()

        back_btn = global_contents.wait_and_get_element(set_capabilities, ios_elements.course_dashboard_back_button)
        assert back_btn.text == values.LANDING_BACK_BUTTON
        back_btn.click()
