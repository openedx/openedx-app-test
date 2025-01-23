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
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin


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

    log.info(f'{globals_contents.target_environment} - '
         f'{globals_contents.login_user_name} - '
         f'{globals_contents.login_password} - '
         f'{globals_contents.android_platform_version} - '
         f'{globals_contents.ios_platform_version}')
    log.info(f'- Setting {globals_contents.target_environment} capabilities')

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
        log.info(f'{values.ERROR_SETTING_CAPS} on - {globals_contents.target_environment}')
        return None

    driver = webdriver.Remote(globals_contents.server_url, desired_capabilities)

    if driver is not None:
        log.info(f'- Setting {globals_contents.target_environment} capabilities are done')
        return driver

    log.info(f'Problem setting {globals_contents.target_environment} capabilities')
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
                                   f'Iteration_{current_day}')
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

@pytest.fixture(scope="module")
def login(set_capabilities, setup_logging):
    """
    Login user based on env given, it will be reusable in tests

    Arguments:
            set_capabilities(webdriver): webdriver object
            setup_logging (logger): logger object

    Returns:
            True: if login is successful
    """

    log = setup_logging
    global_contents = Globals(log)
    android_landing = AndroidLanding(set_capabilities, setup_logging)
    android_sign_in = AndroidSignIn(set_capabilities, setup_logging)
    ios_landing = IosLanding(set_capabilities, setup_logging)
    ios_login = IosLogin(set_capabilities, setup_logging)

    if global_contents.target_environment == values.ANDROID:
        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_signin_button()
        assert android_landing.load_signin_screen().text == values.LOGIN

        assert android_sign_in.get_sign_in_email_label().text == values.EMAIL_OR_USERNAME
        email_field = android_sign_in.get_sign_in_tf_email()
        assert email_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        email_field.send_keys(global_contents.login_user_name)

        assert android_sign_in.get_sign_in_password_label().text == values.PASSWORD
        password_field = android_sign_in.get_sign_in_password_field()
        assert password_field.get_attribute('clickable') == values.TRUE_LOWERCASE
        password_field.send_keys(global_contents.login_password)
        assert android_sign_in.get_signin_button().get_attribute('clickable') == values.TRUE_LOWERCASE
        android_sign_in.get_signin_button().click()
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')

    elif global_contents.target_environment == values.IOS:
        log.info('Login screen successfully loaded')

        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()

        sign_in_button = ios_landing.get_sign_in_button()
        assert ios_landing.get_sign_in_button().text == values.LOGIN
        sign_in_button.click()
        sign_in_title = ios_login.get_sign_in_title()
        assert sign_in_title.text == values.LOGIN

        email_field = ios_login.get_signin_username_textfield()
        assert email_field.text == values.EMAIL_OR_USERNAME_IOS
        email_field.send_keys(global_contents.login_user_name)

        password_title = ios_login.get_signin_password_text()
        assert password_title.text == values.PASSWORD
        password_title.click()
        password_field = ios_login.get_signin_password_textfield()
        assert password_field.get_attribute('value') == values.PASSWORD
        password_field.send_keys(global_contents.login_password)
        password_title.click()
        sign_in_button = ios_login.get_signin_button()
        assert sign_in_button.text == values.LOGIN
        sign_in_button.click()
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')

    return setup_logging

def create_result_directory(target_directory):
    """
    Create directory by specific given name

    Argument:
        target_directory (str): directory name to create
    """

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
