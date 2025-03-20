"""
    What's New Page Module
"""
from appium.webdriver.common.appiumby import AppiumBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosWhatsNew(IosBasePage):
    """
    What's New screen
    """

    def get_close_button(self):
        """
        Get close button

        Returns:
            webdriver element: close Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.whats_new_btn_next
        )

        return self.driver.find_element(AppiumBy.NAME, 'close_button')

    def get_whats_new_msg_title(self):
        """
        Get Whats New message title

        Returns:
            webdriver element: Whats New message title element
        """

        whats_new_msg_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_msg_title
        )
        return whats_new_msg_title

    def get_whats_new_description(self):
        """
        Get Whats New description

        Returns:
            webdriver element: Whats New description element
        """

        whats_new_description = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_description
        )
        return whats_new_description

    def get_next_btn(self):
        """
        Get Next button

        Returns:
            webdriver element: Next button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.whats_new_btn_next
        )

        next_btn = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_btn_next
        )
        return next_btn

    def navigate_features(self):
        """
        Navigate between features

        Returns:
            webdriver element: Done Element
        """

        self.get_next_btn().click()

        if self.get_next_btn().text == 'Done':
            return self.get_next_btn()
        else:
            self.navigate_features()
            return self.get_next_btn()
