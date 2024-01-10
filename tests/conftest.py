"""
   Module ensure environment level initial settings before starting execution
"""

import datetime
import logging.handlers
import os

import pytest
from appium import webdriver

from tests.common import values
from tests.common.globals import Globals


@pytest.fixture(scope="module")
def set_capabilities(setup_logging):
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests

    Arguments:
        setup_logging (logger): logger object

    Returns:
        driver: webdriver object
    """

    log = setup_logging
    globals_contents = Globals(log)
    desired_capabilities = {}

    log.info('{} - {} - {} - {} - {}'.format(
        globals_contents.target_environment,
        globals_contents.login_user_name,
        globals_contents.login_password,
        globals_contents.android_platform_version,
        globals_contents.ios_platform_version
    ))
    log.info('- Setting {} capabilities'.format(globals_contents.target_environment))

    if globals_contents.target_environment == values.ANDROID:
        desired_capabilities['platformName'] = values.ANDROID
        desired_capabilities['platformVersion'] = globals_contents.android_platform_version
        desired_capabilities['deviceName'] = globals_contents.android_device_name
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['appPackage'] = globals_contents.AUT_PACKAGE_NAME
        desired_capabilities['automationName'] = 'UiAutomator2'
        desired_capabilities['newCommandTimeout'] = '0'

    elif globals_contents.target_environment == values.IOS:
        desired_capabilities['platformName'] = values.IOS
        desired_capabilities['platformVersion'] = globals_contents.ios_platform_version
        desired_capabilities['deviceName'] = globals_contents.ios_device_name
        # Required when executing on real iOS device
        desired_capabilities['fullReset'] = True
        desired_capabilities['appWaitDuration'] = '50000'
        desired_capabilities['automationName'] = 'XCUITest'
        desired_capabilities['newCommandTimeout'] = '0'

    else:
        log.info('{} on - {}'.format(values.ERROR_SETTING_CAPS, globals_contents.target_environment))
        return None

    driver = webdriver.Remote(globals_contents.server_url, desired_capabilities)

    if driver is not None:
        log.info('- Setting {} capabilities are done'.format(globals_contents.target_environment))
        return driver
    else:
        log.info('Problem setting {} capabilities'.format(globals_contents.target_environment))
        return None

@pytest.fixture(scope="session")
def setup_logging():
    """
    setup execution logging, it will be reusable in all files

    Returns:
        my_logger: logger object
    """

    current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%M"))

    create_result_directory(values.RESULTS_DIRECTORY)

    iteration_directory = os.path.join(os.path.dirname(__file__), values.RESULTS_DIRECTORY,
                                       'Iteration_{}'.format(current_day))
    create_result_directory(iteration_directory)

    logs_directory = os.path.join(iteration_directory, "logs")
    create_result_directory(logs_directory)

    log_file = os.path.join(os.path.dirname(__file__), logs_directory, values.LOG_FILE_NAME)
    my_logger = logging.getLogger('edX Logs')
    my_logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)
    my_logger.info("Logging is successfully set up")
    return my_logger

def create_result_directory(target_directory):
    """
    Create directory by specific given name

    Argument:
        target_directory (str): directory name to create
    """

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
