"""
    Login Page Module
"""

from appium.webdriver.common.mobileby import MobileBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosLogin(IosBasePage):
    """
    Login screen
    """

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
            webdriver element: Sing In Element
        """

        sign_in_button = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[2]
        return sign_in_button

    def get_password_field(self):
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        password_field = self.driver.find_element(
            MobileBy.CLASS_NAME, ios_elements.password_field)
        return password_field
