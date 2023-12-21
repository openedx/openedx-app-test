"""
   Module ensure environment level initial settings before starting execution
"""

import pytest
from appium import webdriver

from tests.common import values
from tests.common.globals import Globals


@pytest.fixture(scope="module")
def set_capabilities():
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests

    Returns:
        driver: webdriver object
    """

    globals_contents = Globals()
    desired_capabilities = {}

    desired_capabilities['appWaitDuration'] = '50000'
    desired_capabilities['newCommandTimeout'] = '0'

    if globals_contents.target_environment == values.ANDROID:
        desired_capabilities['platformName'] = values.ANDROID
        desired_capabilities['platformVersion'] = globals_contents.android_platform_version
        desired_capabilities['deviceName'] = globals_contents.android_device_name
        desired_capabilities['automationName'] = 'UiAutomator2'

    elif globals_contents.target_environment == values.IOS:
        desired_capabilities['platformName'] = values.IOS
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        desired_capabilities['fullReset'] = True
        desired_capabilities['automationName'] = 'XCUITest'

    else:
        return None

    driver = webdriver.Remote(globals_contents.server_url, desired_capabilities)
