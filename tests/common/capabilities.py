"""Capabilities For Android/iOS on Local/Remote Environments"""

from abc import ABC, abstractmethod
from typing import Dict, Union
from appium.options.common.base import AppiumOptions
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.options.ios.xcuitest.base import XCUITestOptions
from typing import Any

from tests.common.enums import TargetPlatform


class Capabilities(ABC):
    """Platform Dependent Capabilities For Local and Remote Environment"""

    def __init__(self) -> None:
        self._caps: dict[str, Union[bool, str, dict, int]] = {}

    def update(self, updates: Dict) -> None:
        self._caps.update(updates)

    def set(self, key: str, value: Any) -> None:
        self._caps[key] = value

    @abstractmethod
    def get_as_options(self) -> AppiumOptions:
        ...


class AndroidCapabilities(Capabilities):
    """Android Dependent Capabilities For Local and Remote Environment"""

    def __init__(self) -> None:
        super().__init__()

        self._caps.update(
            {
                "appWaitDuration": "50000",
                "gpsEnabled": True,
                "uiautomator2ServerInstallTimeout": 120000,
                "platformName": "Android",
                "appWaitActivity": "*",
                "appium:automationName": "Uiautomator2",
                "autoGrantPermissions": False,
                "newCommandTimeout": 180,
                "appActivity": "org.openedx.app.AppActivity",
                "appPackage" : "org.edx.mobile"
            }
        )

    def get_as_options(self) -> AppiumOptions:
        return UiAutomator2Options().load_capabilities(self._caps)


class IOSCapabilities(Capabilities):
    """iOS Dependent Capabilities For Local and Remote Environment"""

    def __init__(self) -> None:
        super().__init__()
        self._caps.update(
            {
                "appium:automationName": "XCUITest",
                "clearSystemFiles": True,
                "locationServicesEnabled": True,
                "locationServicesAuthorized": True,
                "connectHardwareKeyboard": False,
                "newCommandTimeout": 180,
                "wdaStartupRetries": 3,
                "showXcodeLog": True,
                "platformName": "ios",
                "webviewConnectTimeout": 90000,
                "includeSafariInWebviews": True,
                "safariLogAllCommunication": True,
            }
        )


    def get_as_options(self) -> AppiumOptions:
        return XCUITestOptions().load_capabilities(self._caps)

def caps_factory(platform: TargetPlatform) -> Capabilities:
    if platform == TargetPlatform.ANDROID.value:
        return AndroidCapabilities()
    elif platform == TargetPlatform.IOS.value:
        return IOSCapabilities()
