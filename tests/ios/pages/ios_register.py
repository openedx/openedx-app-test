"""
    Login Page Module
"""
from appium.webdriver.common.mobileby import MobileBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosRegister(IosBasePage):
    """
    Register screen
    """

    def get_register_button(self):
        """
        Get register button

        Returns:
            webdriver element: Register Element
        """

        register_button = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[1]
        return register_button

    def get_register_screen_heading(self):
        """
        Get register screen heading

        Returns:
            webdriver element: Register screen heading Element
        """

        register_heading = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_screen_heading
        )
        return register_heading

    def get_password_field(self):
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        password_field = self.driver.find_element(
            MobileBy.CLASS_NAME, ios_elements.password_field)
        return password_field
