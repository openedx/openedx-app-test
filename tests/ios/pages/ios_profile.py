"""
    Profile Page Module
"""
from appium.webdriver.common.mobileby import MobileBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosProfile(IosBasePage):
    """
    Profile screen
    """

    def get_profile_screen_title(self):
        """
        Get profile screen title

        Returns:
            webdriver element: Profile screen title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.profile_screen_title
        )

        return self.driver.find_element(MobileBy.NAME, 'Profile')

    def get_profile_edit_button(self):
        """
        Get profile edit button

        Returns:
            webdriver element: Profile edit button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_edit_button
        )

    def get_profile_settings_button(self):
        """
        Get profile settings button

        Returns:
            webdriver element: Profile settings button element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.profile_settings_button
        )

    def get_profile_img_profile(self):
        """
        Get profile image

        Returns:
            webdriver element: Profile image element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_user_avatar_image
        )

    def get_profile_user_name_text(self):
        """
        Get user's name text

        Returns:
            webdriver element: User's name text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_user_name_text
        )

    def profile_user_username_text(self):
        """
        Get user's username text

        Returns:
            webdriver element: User's username text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_user_username_text
        )

    def get_profile_settings_text(self):
        """
        Get settings text

        Returns:
            webdriver element: Settings text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_settings_text
        )

    def get_profile_video_settings_button(self):
        """
        Get video settings button

        Returns:
            webdriver element: Video settings button element
        """

        return self.global_contents.get_elements_by_name_ios(
            self.driver,
            ios_elements.profile_video_settings_button
        )[1]

    def get_profile_manage_account_label(self):
        """
        Get manage account label

        Returns:
            webdriver element: Manage account label element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.profile_manage_account_label
        )

    def get_profile_dates_calendar_label(self):
        """
        Get dates calendar label

        Returns:
            webdriver element: Dates & Calendar element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.profile_dates_calendar_label
        )

    def get_profile_support_info_text(self):
        """
        Get support info text

        Returns:
            webdriver element: Support info text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_support_info_text
        )

    def get_profile_tos_text(self):
        """
        Get tos text

        Returns:
            webdriver element: Tos text element
        """

        return self.global_contents.get_element_by_name_ios(
            self.driver,
            'tos'
        )

    def get_profile_privacy_policy(self):
        """
        Get privacy policy

        Returns:
            webdriver element: Privacy policy element
        """

        return self.global_contents.get_element_by_name_ios(
            self.driver,
            ios_elements.profile_privacy_policy
        )

    def get_profile_cookies_policy(self):
        """
        Get cookies policy

        Returns:
            webdriver element: Cookies policy element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_cookies_policy
        )

    def get_profile_dont_sell_data(self):
        """
        Get dont sell data

        Returns:
            webdriver element: Dont sell data element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_dont_sell_data
        )

    def get_profile_contact_support(self):
        """
        Get contact support

        Returns:
            webdriver element: Contact support element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.profile_contact_support
        )

    def get_profile_view_faq(self):
        """
        Get view faq

        Returns:
            webdriver element: View faq element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_view_faq
        )

    def get_profile_version_info(self):
        """
        Get version info

        Returns:
            webdriver element: Version info element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_version_info
        )

    def get_profile_logout_button(self):
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.profile_logout_button
        )

    def get_logout_close_button(self):
        """
        Get close button

        Returns:
            webdriver element: Close button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.logout_close_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.logout_close_button
        )

    def get_logout_dialog_title(self):
        """
        Get dialog title

        Returns:
            webdriver element: Dialog title element
        """

        return self.driver.find_element(MobileBy.NAME, ios_elements.logout_dialog_title)

    def get_logout_button(self):
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self.driver.find_element(MobileBy.NAME, ios_elements.logout_button)

    def get_back_button(self):
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        return self.driver.find_element(MobileBy.NAME, 'arrowLeft')

    def get_videos_back_button(self):
        """
        Get videos settings page

        Returns:
            webdriver element: back element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.main_dashboard_profile_tab
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.main_dashboard_profile_tab
        )

    def get_header_back_button(self):
        """
        Returns:
            element: back button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.back_button_navigation
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.back_button_navigation
        )

    def get_manage_account_title(self):
        """
        Returns:
            element: manage account title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.manage_account_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.manage_account_title
        )
