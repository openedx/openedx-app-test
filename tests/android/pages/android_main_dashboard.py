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

    def get_learn_tab(self):
        """
        Get learn tab

        Returns:
            element: learn fragment element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboard_fragment_learn
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboard_fragment_learn
        )

    def get_profile_tab(self):
        """
        Get profile tab

        Returns:
            element: profile framgent element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashbaord_fragment_profile
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashbaord_fragment_profile
        )
