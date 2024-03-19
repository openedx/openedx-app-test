"""
    Profile Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidProfile(AndroidBasePage):
    """
    Profile screen
    """

    def get_profile_screen_title(self):
        """
        Returns:
            element: profile screen title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_screen_title
        )

    def get_profile_edit_button(self):
        """
        Returns:
            element: profile edit button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_edit_button
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

    def get_profile_username(self):
        """
        Returns:
            element: profile username element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_username
        )

    def get_profile_txt_settings(self):
        """
        Returns:
            element: profile settings element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_settings
        )

    def get_profile_txt_video_settings(self):
        """
        Returns:
            element: profile video settings element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_video_settings
        )

    def get_profile_txt_support_info(self):
        """
        Returns:
            element: profile support info element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_support_info
        )

    def get_profile_txt_contact_support(self):
        """
        Returns:
            element: profile contact support element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_contact_support
        )

    def get_profile_txt_terms_of_use(self):
        """
        Returns:
            element: profile terms of use element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_txt_terms_of_use
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_terms_of_use
        )

    def get_profile_txt_privacy_policy(self):
        """
        Returns:
            element: profile privacy policy element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_privacy_policy
        )

    def get_profile_txt_cookie_policy(self):
        """
        Returns:
            element: profile cookie policy element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_cookie_policy
        )

    def get_profile_personal_info(self):
        """
        Returns:
            element: profile personal info element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_personal_info
        )

    def get_profile_txt_view_faq(self):
        """
        Returns:
            element: profile view faq element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_view_faq
        )

    def get_profile_app_version_code(self):
        """
        Returns:
            element: profile app version code element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_app_version_code
        )

    def get_profile_txt_up_to_date(self):
        """
        Returns:
            element: profile up to date element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_up_to_date
        )

    def get_profile_txt_logout(self):
        """
        Returns:
            element: profile logout element
        """
            
        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_logout
        )

    def get_logout_dialog_title(self):
        """
        Returns:
            element: logout title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.logout_dialog_title
        )

    def get_logout_close_button(self):
        """
        Returns:
            element: logout close button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.logout_close_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.logout_close_button
        )

    def get_logout_button(self):
        """
        Returns:
            element: logout button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.logout_button
        )

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

    def get_edit_profile_leave_button(self):
        """
        Returns:
            element: leave button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.edit_profile_leave_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.edit_profile_leave_button
        )
