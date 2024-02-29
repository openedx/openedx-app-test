"""
    Whats New Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidWhatsNew(AndroidBasePage):
    """
    Whats New screen
    """

    def get_close_button(self):
        """
        Get close button

        Returns:
            element: sign in description element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_close_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_close_button
        )

    def get_whats_new_msg_title(self):
        """
        Get title

        Returns:
            element: whats new title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_msg_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_msg_title
        )

    def get_whats_new_description(self):
        """
        Get description

        Returns:
            element: whats new description element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_description
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_description
        )

    def get_next_btn(self):
        """
        Get next button

        Returns:
            element: next button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_btn_next
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_btn_next
        )

    def navigate_features(self):
        """
        Navigate between features

        Returns:
            webdriver element: Done Element
        """

        self.get_next_btn().click()

        if self.get_done_button():
            return self.get_done_button()
        else:
            self.navigate_features()
            return self.get_done_button()

    def get_done_button(self):
        """
        Get done button

        Returns:
            element: done element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_done_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_done_button
        )
