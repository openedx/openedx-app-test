"""
    Main Dashboard Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidMainDashboard(AndroidBasePage):
    """
    Main Dashboard screen
    """

    def __init__(self):
        super().__init__()
        self._main_dashboard_fragment_discover = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.edx.mobile:id/fragmentDiscover")',
        )
        self._main_dashboard_fragment_learn = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.edx.mobile:id/fragmentLearn")',
        )
        self._main_dashboard_fragment_profile = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.edx.mobile:id/fragmentProfile")',
        )
        self._switcher_label_courses = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Courses")'
        )
        self._switcher_label_program = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Programs")'
        )

    @property
    def discover_tab(self) -> Element:
        """Get discover tab

        Returns:
            Element: sign in description element
        """

        return self._main_dashboard_fragment_discover.find()

    @property
    def learn_tab(self) -> Element:
        """Get learn tab

        Returns:
            Element: learn fragment element
        """

        return self._main_dashboard_fragment_learn

    @property
    def profile_tab(self) -> Element:
        """Get profile tab

        Returns:
            Element: profile fragment element
        """

        return self._main_dashboard_fragment_profile

    @property
    def switcher_label_courses(self) -> Element:
        """Get profile tab

        Returns:
            Element: profile fragment element
        """

        return self._switcher_label_courses

    @property
    def switcher_label_programs(self) -> Element:
        """Get profile tab

        Returns:
            Element: profile fragment element
        """

        return self._switcher_label_program
