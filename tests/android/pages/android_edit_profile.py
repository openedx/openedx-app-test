"""
    Edit Profile Page Module
"""


from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidEditProfile(AndroidBasePage):
    """
    Edit Profile screen
    """

    def __init__(self):
        super().__init__()
        self._edit_profile_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_title")',
        )
        self._done_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_done")'
        )
        self._edit_profile_type_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_type_label")',
        )
        self._edit_profile_user_name = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_user_name")',
        )
        self._edit_profile_limited_profile_message = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_limited_profile_message")',
        )
        self._edit_profile_txt_label_location = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_limited_profile_message")',
        )
        self._edit_profile_tf_select_location = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_select_location")',
        )
        self._edit_profile_txt_label_spoken_language = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_label_spoken_language")',
        )
        self._edit_profile_select_spoken_language = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_select_spoken_language")',
        )
        self._edit_profile_txt_label_about_me = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_label_about_me")',
        )
        self._edit_profile_txt_placeholder_about_me = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_placeholder_about_me")',
        )
        self._profile_img_profile = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("img_profile")'
        )
        self._profile_txt_name = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_profile_name")',
        )
        self._edit_profile_user_image = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("img_edit_profile_user_image")',
        )

    @property
    def edit_profile_title(self) -> Element:
        """
        Returns:
            Element: edit profile title element
        """

        return self._edit_profile_title

    @property
    def get_profile_img_profile(self) -> Element:
        """
        Returns:
            Element: profile image element
        """

        return self._profile_img_profile

    @property
    def get_profile_txt_name(self) -> Element:
        """
        Returns:
            Element: profile text name element
        """

        return self._profile_txt_name

    @property
    def done_button(self) -> Element:
        """
        Returns:
            Element: Done button element
        """

        return self._done_button

    @property
    def edit_profile_type_label(self) -> Element:
        """
        Returns:
            Element: edit profile type label element
        """

        return self._edit_profile_type_label

    @property
    def get_edit_profile_user_image(self) -> Element:
        """
        Returns:
            Element: edit profile user image element
        """

        return self._edit_profile_user_image

    @property
    def edit_profile_user_name(self) -> Element:
        """
        Returns:
            Element: edit profile user name element
        """

        return self._edit_profile_user_name

    @property
    def edit_profile_limited_profile_message(self) -> Element:
        """
        Returns:
            Element: edit profile limited profile message element
        """

        return self._edit_profile_limited_profile_message

    @property
    def edit_profile_txt_label_location(self) -> Element:
        """
        Returns:
            Element: edit profile location label element
        """

        return self._edit_profile_txt_label_location

    @property
    def profile_tf_select_location(self) -> Element:
        """
        Returns:
            Element: edit profile select location element
        """

        return self._edit_profile_tf_select_location

    @property
    def edit_profile_select_spoken_language(self) -> Element:
        """
        Returns:
            Element: edit profile select spoken language element
        """

        return self._edit_profile_select_spoken_language

    @property
    def edit_profile_txt_label_spoken_language(self) -> Element:
        """
        Returns:
            Element: edit profile label spoken language element
        """

        return self._edit_profile_txt_label_spoken_language

    @property
    def edit_profile_txt_label_about_me(self) -> Element:
        """
        Returns:
            Element: edit profile label about me element
        """

        return self._edit_profile_txt_label_about_me

    @property
    def edit_profile_txt_placeholder_about_me(self) -> Element:
        """
        Returns:
            Element: edit profile placeholder about me element
        """

        return self._edit_profile_txt_placeholder_about_me
