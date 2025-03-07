"""
   Module ensure environment level initial settings before starting execution
"""

import datetime
import logging.handlers
import os
from typing import Optional

import pytest
from pytest_html import extras as pytest_html_extras
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException

from tests.common import values
from tests.common.globals import Globals
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import utils
from tests.common.utils import sanitize_name, get_formatted_datetime
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin




def is_test_failed(report: pytest.TestReport) -> bool:
    x_fail = hasattr(report, "wasxfail")
    return (report.skipped and x_fail) or (report.failed and not x_fail)

def is_controller_node(config: pytest.Config) -> bool:
    return not hasattr(config, "workerinput")

def report_screenshot():
    """
    Get screenshots of the different screens
    Arguments:
    Returns:
        str : file path
    """
    try:
        file_path = (
            f"{SessionData.screenshots_directory}/{SessionData.test_case_name}_"
            f"{get_formatted_datetime()}.png"
        )
        SessionData.driver.save_screenshot(file_path)
        return (
            '<div><img src="{}" alt="screenshot" style="width:304px;height:228px;" '
            'onclick="window.open(this.src)" align="right"/></div>'.format(file_path)
        )

    except Exception:
        pass

@pytest.fixture(scope="module")
def set_capabilities(setup_logging, request):
    """
    set_capabilities will setup environment capabilities based on
    environment given, and return driver object accessible in all Tests

    Arguments:
        setup_logging (logger): logger object
        request: (_pytest.fixtures.SubRequest): request object

    Returns:
        driver: webdriver object
    """

    log = setup_logging
    globals_contents = Globals(log)
    desired_capabilities = {}
    SessionData.globals_contents = globals_contents
    SessionData.test_case_name = str(request.node.name).replace(".py", "")

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
        desired_capabilities['appActivity'] = 'org.openedx.app.AppActivity'
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
        SessionData.driver = driver
        return driver

    log.info(f'Problem setting {globals_contents.target_environment} capabilities')
    return None

@pytest.fixture(scope="module")
def setup_logging(request) -> logging.Logger:
    """
    setup execution logging, it will be reusable in all files

    Returns:
        my_logger: logger object
    """
    test_case_name = str(request.node.name).replace(".py", "")
    current_directory = os.path.dirname(__file__)
    # main results directory
    utils.create_directory(values.RESULTS_DIRECTORY)
    # main iteration directory
    utils.create_directory(SessionData.iteration_directory_base)

    SessionData.iteration_directory = str(os.path.join(
        current_directory, values.RESULTS_DIRECTORY, SessionData.iteration_directory_base, test_case_name
    ))

    utils.create_directory(SessionData.iteration_directory)

    SessionData.screenshots_directory = os.path.join(current_directory, SessionData.iteration_directory)
    log_file = os.path.join(current_directory, SessionData.iteration_directory, values.LOG_FILE_NAME)

    my_logger = logging.getLogger('edX Automation Logs')
    my_logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)

    def finalizer():
        """finalizer run when test case finishes"""

        my_logger.info(f"================logging Stopped=====================")
        log_handler.close()

    request.addfinalizer(finalizer)

    my_logger.info("=================Logging is successfully set up=================")
    return my_logger

def pytest_configure(config: pytest.Config):
    """
    called after command line options have been parsed
    and all plugins and initial conftest files been loaded
    """
    marker = config.getoption("-m")

    if is_controller_node(config):
        job_id = datetime.datetime.now().strftime("%Y_%m_%d__%H:%M_")
        iteration_name = f"{marker}_{job_id}" if marker else f"Iteration_{job_id}_android"
        iteration_name = sanitize_name(iteration_name)
        config.iteration_name = iteration_name
    else:
        iteration_name: str = config.workerinput["iterationName"]

    SessionData.iteration_directory_base = str(
        os.path.join(os.path.dirname(__file__), values.RESULTS_DIRECTORY, iteration_name.lower())
    )
    SessionData.iteration_name = iteration_name

    config.option.htmlpath = os.path.join(
        SessionData.iteration_directory_base, f"{iteration_name}{values.HTML_REPORT_FILE_NAME}"
    )


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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    """
    Adds screenshot to HTML report when test fails

    """
    outcome = yield
    report: pytest.TestReport = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":

        try:
            if SessionData.driver and is_test_failed(report):
                html = report_screenshot()
                extras.append(pytest_html_extras.html(html))
                report.extras = extras

        except WebDriverException as wde:
            SessionData.globals_contents.project_log.error(f"Failed to Quit Session: {wde}")


class SessionData:
    """class for keeping necessary session related info"""

    iteration_directory_base: str
    iteration_video_directory_base: str = None
    globals_contents: Globals = None
    driver: WebDriver = None
    screenshots_directory = None
    test_case_name = None
    is_case_running = True
    iteration_directory: Optional[str] = None
    iteration_name = None
    target_environment = None

    @staticmethod
    def reset():
        """reset critical session related info"""

        SessionData.driver = None
        SessionData.globals_contents = None
