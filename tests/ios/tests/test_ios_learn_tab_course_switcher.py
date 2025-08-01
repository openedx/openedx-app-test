"""Test Module for Course Switcher in iOS Learn Tab"""

from framework import expect
from framework.element import Element
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList


class TestIosCourseSwitcher:
    """
    Test class for validating course switcher functionality in iOS Learn tab.
    """

    def test_validate_programs_switcher(self, ios_login, setup_logging):
        """
        Scenarios:
           Verify following contents are visible on screen,
               Courses switcher
               Profile Tab, Programs Tab, Profiel tab
           Verify that clicking courses switcher will open dropdown
           Verify that dropdown has courses and programs options in it
           Verify that clicking each menu will load its screen
        """
        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        global_contents = Globals(setup_logging)
        main_dashboard = IosMainDashboard()
        my_courses_list = IosMyCoursesList()

        main_dashboard.learn_tab.click()
        switcher_label = my_courses_list.courses_dropdown_menu
        expect(switcher_label).to_have("Courses", ElementAttribute.LABEL)
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(driver, "Courses")
        assert switcher_label.get_attribute("label") == "Courses"
        programs_switcher = global_contents.wait_and_get_element(driver, "Programs")
        assert programs_switcher.text == "Programs"
        course_switcher.click()
        assert switcher_label.get_attribute("label") == "Courses"
        switcher_label.click()
        programs_switcher = global_contents.wait_and_get_element(driver, "Programs")
        programs_switcher.click()
        assert switcher_label.get_attribute("label") == "Programs"
        switcher_label.click()
        course_switcher = global_contents.wait_and_get_element(driver, "Courses")
        course_switcher.click()
        assert switcher_label.get_attribute("label") == "Courses"
