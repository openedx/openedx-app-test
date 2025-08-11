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
        self._back_navigation_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ib_back")')
        self._text_view = Element(AppiumBy.CLASS_NAME, "android.widget.TextView")
        self._android_native_permission_allow_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")',
        )
        self._android_native_permission_revoke_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_deny_button")',
        )
        self._android_loading_circle = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ProgressBar")'
        )
        self._sb_search_field = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("sb_search")')
        self._chrome_sign_in_dismiss_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("com.android.chrome:id/signin_fre_dismiss_button")',
        )
        self._chrome_notifications_dismiss_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.chrome:id/negative_button")'
        )
        self._edx_feedback_google_form_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("edX Mobile Apps Feedback")'
        )
        self._ai_assistant_dismiss_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Close proactive message")',
        )
        self._edit_text_view = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")'
        )
        self._android_progress_bar = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ProgressBar")'
        )
        self._text_element_selector = 'new UiSelector().text("{}")'
        self._accept_cookies_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("onetrust-accept-btn-handler")'
        )

    @property
    def sb_search_field(self) -> Element:
        """Get search field

        Returns:
            Element: search field element
        """
        return self._sb_search_field

    @property
    def android_loading_circle(self) -> Element:
        """Get loading circle

        Returns:
            Element: loading circle element
        """
        return self._android_loading_circle

    @property
    def android_progress_bar(self) -> Element:
        """Get android progress bar

        Returns:
            Element: android progress bar element
        """
        return self._android_progress_bar

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

    @property
    def chrome_sign_in_dismiss_button(self) -> Element:
        """Get dismiss button

        Returns:
            Element: dismiss button
        """

        return self._chrome_sign_in_dismiss_button

    @property
    def chrome_notifications_dismiss_button(self) -> Element:
        """Get dismiss button

        Returns:
            Element: dismiss button
        """

        return self._chrome_notifications_dismiss_button

    @property
    def edx_feedback_google_form_title(self) -> Element:
        """Get dismiss button

        Returns:
            Element: dismiss button
        """

        return self._edx_feedback_google_form_title

    @property
    def edit_text_view(self) -> Element:
        """edit text view

        Returns:
            Element: edit text view
        """

        return self._edit_text_view

    @property
    def ai_assistant_dismiss_button(self) -> Element:
        """Get dismiss button

        Returns:
            Element: dismiss button
        """

        return self._ai_assistant_dismiss_button

    @property
    def accept_cookies_button(self) -> Element:
        """Get accept cookies button

        Returns:
            Element: accept cookies button
        """

        return self._accept_cookies_button

    def find_by_text_on_screen(self, text: str, raise_error: bool = True) -> Element | None:
        """Find element by text.
        Returns:
            Element: element with required text
        """
        if text:
            selector = self._text_element_selector.format(text)
            return Element(AppiumBy.ANDROID_UIAUTOMATOR, selector).find(raise_exception=raise_error)
        raise ValueError("text cannot be empty")

    def get_text_element_instance(self, text: str) -> Element:
        """Element by text.
        Returns:
            Element: element with required text
        """
        if text:
            selector = self._text_element_selector.format(text)
            return Element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
        raise ValueError("text cannot be empty")

    def find_by_partial_text_on_screen(self, text: str, raise_error: bool = True) -> Element:
        """Find element by text.
        Returns:
            Element: element with required text
        """
        if text:
            selector = f'new UiSelector().textContains("{text}")'
            return Element(AppiumBy.ANDROID_UIAUTOMATOR, selector).find(raise_exception=raise_error)
        raise ValueError("text cannot be empty")
