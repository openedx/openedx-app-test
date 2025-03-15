"""
    Profile Page Module
"""

from framework.element import Element
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidProfile(AndroidBasePage):
    """
    Profile screen
    """
    def __init__(self):
        super().__init__()
        self._settings_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Settings")')
        self._profile_img_profile = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("img_profile")')
        self._profile_txt_name = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_name")')
        self._profile_username = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_username")')
        self._edit_profile_btn = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile")')
        self._privacy_policy = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Privacy Policy")')
        self._logout_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log Out")')
        self._logout_prompt_logout_button_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_logout")')


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

    @property
    def profile_img_profile(self) -> Element:
        """
        Returns:
            element: profile image element
        """

        return self._profile_img_profile

    @property
    def profile_txt_name(self) -> Element:
        """
        Returns:
            element: profile text name element
        """

        return self._profile_txt_name

    @property
    def profile_username(self) -> Element:
        """
        Returns:
            element: profile username element
        """

        return self._profile_username

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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_txt_video_settings
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.profile_txt_video_settings
        )

    def get_profile_txt_support_info(self):
        """
        Returns:
            element: profile support info element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_support_info)

    def get_profile_txt_contact_support(self):
        """
        Returns:
            element: profile contact support element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_contact_support
        )

    def get_profile_txt_terms_of_use(self):
        """
        Returns:
            element: profile terms of use element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_terms_of_use
        )

    @property
    def privacy_policy_text(self) -> Element:
        """
        Returns:
            element: profile privacy policy element
        """

        return self._privacy_policy

    def get_profile_txt_cookie_policy(self):
        """
        Returns:
            element: profile cookie policy element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_cookie_policy
        )

    def get_profile_personal_info(self):
        """
        Returns:
            element: profile personal info element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_personal_info
        )

    def get_profile_txt_view_faq(self):
        """
        Returns:
            element: profile view faq element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_txt_view_faq
        )

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_view_faq
        )

    def get_profile_app_version_code(self):
        """
        Returns:
            element: profile app version code element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_app_version_code
        )

    def get_profile_txt_up_to_date(self):
        """
        Returns:
            element: profile up to date element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_txt_up_to_date
        )

    @property
    def profile_txt_logout(self) -> Element:
        """
        Returns:
            element: profile logout element
        """

        return self._logout_text

    def get_logout_dialog_text(self):
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

    @property
    def logout_prompt_logout_button_text(self) -> Element:
        """
        Returns:
            element: logout button element
        """

        return self._logout_prompt_logout_button_text

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

    def get_logout_dialog_title(self):
        """
        Returns:
            element: logout dialog title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashbaord_fragment_profile
        )

        profile_tab = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashbaord_fragment_profile
        )
        profile_tab.click()
        return profile_tab.get_attribute('selected')

    @property
    def settings_button(self) -> Element:
        """
        Returns:
            element: settings button element
        """

        return self._settings_button

    def get_settings_screen_title(self):
        """
        Returns:
            element: settings screen title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.profile_screen_title
        )

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_settings_txt)

    def get_manage_account_label(self):
        """
        Returns:
            element: manage account label element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_manage_account_label)

    def get_video_label(self):
        """
        Returns:
            element: video label element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_video_label)

    def get_dates_calendar_label(self):
        """
        Returns:
            element: Dates & Calendar label element
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.profile_dates_calendar_label)

    @property
    def edit_profile_button(self) -> Element:
        """
        Returns:
            element: edit profile button element
        """

        return self._edit_profile_btn
