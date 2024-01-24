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

        sign_in_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.logistration_signin_button
        )
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

    def get_signin_heading(self):
        """
        Get singin text

        Returns:
            webdriver element: Singin heading element
        """

        sign_in_heading = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.logistration_signin_button
        )
        return sign_in_heading
