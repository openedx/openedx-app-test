"""
    Edit Profile Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.mobileby import MobileBy


class AndroidEditProfile(AndroidBasePage):
    """
    Edit Profile screen
    """

    def get_edit_profile_title(self):
        """
        Returns:
            element: edit profile title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_title
        )

    def get_profile_img_profile(self):
        """
        Returns:
            element: profile image element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_img_profile
        )

    def get_profile_txt_name(self):
        """
        Returns:
            element: profile text name element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_name
        )

    def get_save_changes_button(self):
        """
        Returns:
            element: save changes button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.save_changes_button
        )

    def get_back_button(self):
        """
        Returns:
            element: back button element
        """

        return self.global_contents.get_back_button(
            self.driver
        )

    def get_done_button(self):
        """
        Returns:
            element: Done button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_done_button
        )

    def get_edit_profile_type_label(self):
        """
        Returns:
            element: edit profile type label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_type_label
        )

    def get_edit_profile_user_image(self):
        """
        Returns:
            element: edit profile user image element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_user_image
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_user_image
        )

    def get_edit_profile_user_name(self):
        """
        Returns:
            element: edit profile user name element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_user_name
        )

    def get_edit_profile_limited_profile_message(self):
        """
        Returns:
            element: edit profile limited profile message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_limited_profile_message
        )

    def get_edit_profile_txt_label_location(self):
        """
        Returns:
            element: edit profile location label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_txt_label_location
        )

    def get_edit_profile_tf_select_location(self):
        """
        Returns:
            element: edit profile select location element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_tf_select_location
        )

    def get_edit_profile_select_spoken_language(self):
        """
        Returns:
            element: edit profile select spoken language element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_select_spoken_language
        )

    def get_edit_profile_txt_label_spoken_language(self):
        """
        Returns:
            element: edit profile label spoken language element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_txt_label_spoken_language
        )

    def get_edit_profile_txt_label_about_me(self):
        """
        Returns:
            element: edit profile label about me element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_txt_label_about_me
        )

    def get_edit_profile_txt_placeholder_about_me(self):
        """
        Returns:
            element: edit profile placeholder about me element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_txt_placeholder_about_me
        )
