"""
    Course Dashboard Home Tab Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_course_home_tab import AndroidCourseHomeTab
from tests.common import values
from tests.common.globals import Globals


class TestAndroidCourseHomeTab:
    """
    Course Dashboard screen's Test Case
    """

    def test_start_course_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidCourseHomeTab.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        if login and global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == 'Done'
            whats_new_page.get_done_button().click()

        learn_tab = main_dashboard_page.get_learn_tab()
        assert learn_tab.get_attribute('content-desc') == values.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == values.TRUE_LOWERCASE

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
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

        course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        second_course_name = global_contents.get_element_by_text(set_capabilities, values.MY_COURSES_SECOND_COURSE_NAME)
        assert second_course_name.text == values.MY_COURSES_SECOND_COURSE_NAME
        second_course_name.click()
        if course_dashboard_page.get_allow_notifications_button():
            course_dashboard_page.get_allow_notifications_button().click()

        home_tab = course_dashboard_page.get_course_dashboard_home_tab()
        assert home_tab.text == values.COURSE_DASHBOARD_HOME_TAB

        deadline_title = global_contents.get_element_by_text(set_capabilities, values.COURSE_MISSED_DEADLINES_LABEL)
        assert deadline_title.text == values.COURSE_MISSED_DEADLINES_LABEL

        deadline_description = global_contents.get_element_by_text(set_capabilities, values.COURSE_DEADLINE_DESCRIPTION_LABEL)
        assert deadline_description.text == values.COURSE_DEADLINE_DESCRIPTION_LABEL

        shift_due_dates_button = global_contents.get_element_by_text(set_capabilities, values.COURSE_SHIFT_DUE_DATES)
        assert shift_due_dates_button.text == values.COURSE_SHIFT_DUE_DATES

        continue_with_lable = global_contents.get_element_by_text(set_capabilities, values.COURSE_CONTINUE_WITH_LABEL)
        assert continue_with_lable.text == values.COURSE_CONTINUE_WITH_LABEL

        resume_button = global_contents.get_element_by_text(set_capabilities, values.COURSE_RESUME_BUTTON)
        assert resume_button.text == values.COURSE_RESUME_BUTTON

        global_contents.scroll_from_element(set_capabilities, resume_button)
        introduction_section = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_SECTION_LABEL)
        assert introduction_section.text == values.COURSE_SECTION_LABEL
        introduction_section.click()

        subsection_elem = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_SUBSECTION_LABEL)
        assert subsection_elem.text == values.COURSE_SUBSECTION_LABEL
        subsection_elem.click()

        component_header_title = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_SUBSECTION_LABEL)
        assert component_header_title.text == values.COURSE_SUBSECTION_LABEL

        back_btn = global_contents.get_element_by_description_android(set_capabilities, values.LANDING_BACK_BUTTON)
        assert back_btn.get_attribute('content-desc') == values.LANDING_BACK_BUTTON
        back_btn.click()
        global_contents.scroll_from_element(set_capabilities, component_header_title)

        section1_elem = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_SECTION_1_LABEL)
        assert section1_elem.text == values.COURSE_SECTION_1_LABEL
        section1_elem.click()

        subsection1_elem = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_SUBSECTION_1_LABEL)
        assert subsection1_elem.text == values.COURSE_SUBSECTION_1_LABEL

        homework_elem = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_COMPONENT_LABEL)
        assert homework_elem.text == values.COURSE_COMPONENT_LABEL
        homework_elem.click()

        component_header = global_contents.get_android_element_by_text(set_capabilities, values.COURSE_COMPONENT_LABEL)
        assert component_header.text == values.COURSE_COMPONENT_LABEL

    def test_component_navigation_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify next button element and it is clickable
            Verify previous button element and it is clickable
            Verify user can click on next button until finish button appears
            Verify clicking finish button will load the celebratory modal
            Verify Back to outline button on Modal and clicking this button
                loads the compoenents screen
            Verify clicking on back button will navigate the user to dashboard page
        """

        global_contents = Globals(setup_logging)
        course_home_page = AndroidCourseHomeTab(set_capabilities, setup_logging)

        next_btn = course_home_page.get_next_btn()
        assert next_btn.text == values.COURSE_COMPONENT_NEXT_BUTTON
        next_btn.click()

        prev_btn = course_home_page.get_prev_btn()
        assert prev_btn.text == values.COURSE_COMPONENT_PREVIOUS_BUTTON
        prev_btn.click()

        finish_button = course_home_page.component_navigation()
        assert finish_button.text == values.COURSE_COMPONENT_FINISH_BUTTON
        finish_button.click()

        back_to_outline = global_contents.get_android_element_by_text(
            set_capabilities, values.COURSE_COMPLETION_BACK_BUTTON)
        assert back_to_outline.text == values.COURSE_COMPLETION_BACK_BUTTON
        back_to_outline.click()

        back_btn = global_contents.get_element_by_description_android(set_capabilities, values.LANDING_BACK_BUTTON)
        assert back_btn.get_attribute('content-desc') == values.LANDING_BACK_BUTTON
        back_btn.click()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        profile_page = AndroidProfile(set_capabilities, setup_logging)
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        profile_tab = main_dashboard_page.get_profile_tab()
        profile_tab.click()
        profile_page.get_settings_button().click()
        global_contents.scroll_from_element(set_capabilities, profile_page.get_profile_txt_privacy_policy())

        profile_page.get_profile_txt_logout().click()
        assert profile_page.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        profile_page.get_logout_button().click()
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
