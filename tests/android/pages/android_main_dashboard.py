"""
    Main Dashboard Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidMainDashboard(AndroidBasePage):
    """
    Main Dashbaord screen
    """

    def get_discover_tab(self):
        """
        Get discover tab

        Returns:
            element: sign in description element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_fragment_discover
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_fragment_discover
        )

    def get_dashboard_tab(self):
        """
        Get discover tab

        Returns:
            element: discover fragment element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_fragment_dashboard
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_fragment_dashboard
        )

    def get_programs_tab(self):
        """
        Get programs tab

        Returns:
            element: programs fragment element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_fragment_programs
        )

    def get_profile_tab(self):
        """
        Get profile tab

        Returns:
            element: profile framgent element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashbaord_fragment_profile
        )
