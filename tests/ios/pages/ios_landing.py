"""
    New Landing Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosLanding(IosBasePage):
    """
    New Landing screen
    """

    def get_search_courses_field(self):
        """
        Get search courses field

        Returns:
            webdriver element: search courses field element
        """

        search_courses_field = self.global_contents.get_ios_all_editfields(
            self.driver
            )[0]
        return search_courses_field

    def get_welcome_message(self):
        """
        Get welcome message

        Returns:
            webdriver element: welcome message element
        """

        welcome_message = self.global_contents.get_ios_all_static_text(
            self.driver
            )[0]
        return welcome_message

    def get_search_title(self):
        """
        Get search title

        Returns:
            webdriver element: search title element
        """

        search_title = self.global_contents.get_ios_all_static_text(
            self.driver
            )[1]
        return search_title
