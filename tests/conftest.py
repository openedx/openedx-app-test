"""
   Module ensure environment level initial settings before starting execution
"""

import pytest
from appium import webdriver

from tests.common import strings
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

    if globals_contents.target_environment == strings.ANDROID:
        desired_capabilities['platformName'] = strings.ANDROID
        desired_capabilities['platformVersion'] = globals_contents.android_platform_version
        desired_capabilities['deviceName'] = globals_contents.android_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['automationName'] = 'UiAutomator2'
        desired_capabilities['newCommandTimeout'] = '0'

    elif globals_contents.target_environment == strings.IOS:
        desired_capabilities['platformName'] = strings.IOS
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        desired_capabilities['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['automationName'] = 'XCUITest'
        desired_capabilities['newCommandTimeout'] = '0'

    else:
        return None

    driver = webdriver.Remote(globals_contents.server_url, desired_capabilities)

    if driver is not None:
        def fin(request):
            # Quit the Appium driver after the test
            request.addfinalizer(fin)
        return driver
    else:
        return None
