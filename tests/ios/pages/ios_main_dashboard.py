"""
    Main Dashboard Page Module
"""
from appium.webdriver.common.appiumby import AppiumBy

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosMainDashboard(IosBasePage):
    """
    Main Dashboard screen
    """

    def get_close_button(self):
        """
        Get close button

        Returns:
            webdriver element: close Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver, ios_elements.whats_new_btn_next
        )

        return self.driver.find_element(AppiumBy.NAME, "close_button")

    def get_main_dashboard_discover_tab(self):
        """
        Get discover tab

        Returns:
            webdriver element: Discover tab element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver, ios_elements.main_dashboard_discover_tab
        )

        discover_tab = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.main_dashboard_discover_tab
        )
        return discover_tab

    def get_main_dashboard_learn_tab(self):
        """
        Get discover tab

        Returns:
            webdriver element: Discover tab element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver, ios_elements.main_dashboard_learn_tab
        )

        discover_tab = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.main_dashboard_learn_tab
        )
        return discover_tab

    def get_main_dashboard_programs_tab(self):
        """
        Get programs tab

        Returns:
            webdriver element: Programs tab element
        """

        programs_tab = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.main_dashboard_programs_tab
        )
        return programs_tab

    def get_main_dashboard_tab(self):
        """
        Get dashbaord tab

        Returns:
            webdriver element: Dashboard tab element
        """

        dashboard = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.main_dashboard_tab
        )
        return dashboard

    def get_main_dashboard_profile_tab(self):
        """
        Get profile tab

        Returns:
            webdriver element: profile tab element
        """

        profile_tab = self.global_contents.get_element_by_name_ios(
            self.driver, "Profile"
        )
        return profile_tab
