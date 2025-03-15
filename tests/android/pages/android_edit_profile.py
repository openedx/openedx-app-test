"""
    Edit Profile Page Module
"""

from framework.element import Element
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidEditProfile(AndroidBasePage):
    """
    Edit Profile screen
    """
    def __init__(self):
        super().__init__()
        self._edit_profile_title = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile_title")')
        self._done_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_done")')
        self._edit_profile_type_label = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile_type_label")')
        self._edit_profile_user_name = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile_user_name")')
        self._edit_profile_limited_profile_message = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile_limited_profile_message")')
        self._edit_profile_txt_label_location = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile_limited_profile_message")')
        self._edit_profile_tf_select_location = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_select_location")')
        self._edit_profile_txt_label_spoken_language = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_label_spoken_language")')
        self._edit_profile_select_spoken_language = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_select_spoken_language")')
        self._edit_profile_txt_label_about_me = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_label_about_me")')
        self._edit_profile_txt_placeholder_about_me = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_placeholder_about_me")')

    @property
    def edit_profile_title(self) -> Element:
        """
        Returns:
            element: edit profile title element
        """

        return self._edit_profile_title

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

    @property
    def done_button(self):
        """
        Returns:
            element: Done button element
        """

        return self._done_button

    @property
    def edit_profile_type_label(self):
        """
        Returns:
            element: edit profile type label element
        """

        return self._edit_profile_type_label

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

    @property
    def edit_profile_user_name(self):
        """
        Returns:
            element: edit profile user name element
        """

        return self._edit_profile_user_name

    @property
    def edit_profile_limited_profile_message(self):
        """
        Returns:
            element: edit profile limited profile message element
        """

        return self._edit_profile_limited_profile_message

    @property
    def edit_profile_txt_label_location(self):
        """
        Returns:
            element: edit profile location label element
        """

        return self._edit_profile_txt_label_location

    @property
    def profile_tf_select_location(self):
        """
        Returns:
            element: edit profile select location element
        """

        return self._edit_profile_tf_select_location

    @property
    def edit_profile_select_spoken_language(self):
        """
        Returns:
            element: edit profile select spoken language element
        """

        return self._edit_profile_select_spoken_language

    @property
    def edit_profile_txt_label_spoken_language(self):
        """
        Returns:
            element: edit profile label spoken language element
        """

        return self._edit_profile_txt_label_spoken_language

    @property
    def edit_profile_txt_label_about_me(self):
        """
        Returns:
            element: edit profile label about me element
        """

        return self._edit_profile_txt_label_about_me

    @property
    def edit_profile_txt_placeholder_about_me(self):
        """
        Returns:
            element: edit profile placeholder about me element
        """

        return self._edit_profile_txt_placeholder_about_me
