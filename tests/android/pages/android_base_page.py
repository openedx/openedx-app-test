"""
   Module covers Android base page
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element


class AndroidBasePage:
    """
    Base page for all Android Pages
    """

    def __init__(self):
        self.textview_drawer_account_option = None
        self.account_logout_option = None
        self.target_activity = None
        self._text_toolbar_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_toolbar_title")',
        )
        self._screen_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_screen_title")',
        )
        self._back_navigation_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("ib_back")'
        )
        self._text_view = Element(AppiumBy.CLASS_NAME, "android.widget.TextView")
        self._android_native_permission_allow_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")',
        )
        self._android_native_permission_revoke_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_deny_button")',
        )

    @property
    def text_toolbar_title(self) -> Element:
        """Get toolbar title

        Returns:
            Element: toolbar title element
        """

        return self._text_toolbar_title

    @property
    def screen_title(self) -> Element:
        """Get screen title
        Returns:
            Element: screen title
        """
        return self._screen_title

    @property
    def back_navigation_button(self) -> Element:
        """Navigate back
        Returns:
            Element: back navigation button
        """
        return self._back_navigation_button

    @property
    def text_view(self) -> Element:
        """Text view widget
        Returns:
            Element: text view element
        """
        return self._text_view

    @property
    def allow_notifications_button(self) -> Element:
        """Get Allow button

        Returns:
            Element: allow permissions button
        """

        return self._android_native_permission_allow_button

    @property
    def revoke_notifications_button(self) -> Element:
        """Get revoke button

        Returns:
            Element: revoke permission button
        """

        return self._android_native_permission_allow_button

    def find_by_text_on_screen(self, text: str) -> Element:
        """Find element by text.
        Returns:
            Element: element with required text
        """
        if text:
            return Element(
                AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")'
            ).find()
        raise ValueError("text cannot be empty")
