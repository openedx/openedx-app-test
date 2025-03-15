"""
Module ensure environment level initial settings before starting execution
"""

import datetime
import logging.handlers
import os
from typing import Optional

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from pytest_html import extras as pytest_html_extras
from selenium.common.exceptions import WebDriverException

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_whats_new import AndroidWhatsNew
from framework import expect
from framework.element import Element
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import utils, values
from tests.common.capabilities import caps_factory
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.common.utils import get_formatted_datetime, sanitize_name
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew


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
            f"{SessionData.screenshots_directory}/{SessionData.test_case_name}_" f"{get_formatted_datetime()}.png"
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

    logger: logging.Logger = setup_logging
    globals_contents = Globals(logger)
    capabilities = caps_factory(globals_contents.target_environment)
    desired_capabilities = {}
    SessionData.globals_contents = globals_contents
    SessionData.test_case_name = os.path.basename(str(request.node.name)).replace(".py", "")
    logger.info(
        f"{globals_contents.target_environment} - "
        f"{globals_contents.login_user_name} - "
        f"{globals_contents.login_password} - "
        f"{globals_contents.platform_version} - "
    )
    logger.info(f"- Setting {globals_contents.target_environment} capabilities")

    desired_capabilities["appium:platformVersion"] = globals_contents.platform_version
    desired_capabilities["appium:fullReset"] = globals_contents.full_reset
    if globals_contents.app_path:
        desired_capabilities["appium:app"] = globals_contents.app_path
    if globals_contents.device_name:
        desired_capabilities["appium:deviceName"] = globals_contents.device_name

    capabilities.update(desired_capabilities)
    setup_logging.info(f"Requesting session with capabilities:{capabilities.get_as_options()}")
    driver = webdriver.Remote(globals_contents.server_url, options=capabilities.get_as_options())

    if driver is not None:
        logger.info(f"- Setting {globals_contents.target_environment} capabilities are done")
        SessionData.driver = driver
        return driver

    logger.info(f"Problem setting {globals_contents.target_environment} capabilities")
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
    test_case_name = os.path.basename(str(request.node.name)).replace(".py", "")
    SessionData.iteration_directory = str(
        os.path.join(
            current_directory,
            values.RESULTS_DIRECTORY,
            SessionData.iteration_directory_base,
            test_case_name,
        )
    )

    utils.create_directory(SessionData.iteration_directory)

    SessionData.screenshots_directory = os.path.join(current_directory, SessionData.iteration_directory)
    log_file = os.path.join(current_directory, SessionData.iteration_directory, values.LOG_FILE_NAME)

    my_logger = logging.getLogger("edX Automation Logs")
    my_logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)

    def finalizer():
        """finalizer run when test case finishes"""

        my_logger.info("================logging Stopped=====================")
        log_handler.close()

    request.addfinalizer(finalizer)

    my_logger.info("=================Logging is successfully set up=================")
    my_logger.info(f"@@@ current dir: {current_directory}")
    my_logger.info(f"@@@ base iteration dir: {SessionData.iteration_directory_base}")
    my_logger.info(f"@@@ iteration dir: {SessionData.iteration_directory}")
    my_logger.info(f"@@@ node name : {str(request.node.name)}")

    return my_logger


def pytest_configure(config: pytest.Config):
    """
    called after command line options have been parsed
    and all plugins and initial conftest files been loaded
    """
    marker = config.getoption("-m")

    if is_controller_node(config):
        job_id = datetime.datetime.now().strftime("%Y_%m_%d__%H:%M_")
        iteration_name = f"{marker}_{job_id}" if marker else f"Iteration_{job_id}"
        iteration_name = sanitize_name(iteration_name)
        config.iteration_name = iteration_name
    else:
        iteration_name: str = config.workerinput["iterationName"]

    SessionData.iteration_directory_base = str(
        os.path.join(os.path.dirname(__file__), values.RESULTS_DIRECTORY, iteration_name.lower())
    )
    SessionData.iteration_name = iteration_name

    config.option.htmlpath = os.path.join(
        SessionData.iteration_directory_base,
        f"{iteration_name}{values.HTML_REPORT_FILE_NAME}",
    )


@pytest.fixture(scope="module")
def android_login(set_capabilities, setup_logging):
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
    Element.set_driver(set_capabilities)
    Element.set_logger(setup_logging)
    android_landing = AndroidLanding()
    android_sign_in = AndroidSignIn()
    whats_new_page = AndroidWhatsNew()
    main_dashboard_page = AndroidMainDashboard()
    profile_page = AndroidProfile()

    expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
    assert android_landing.signin_button.exists()
    assert android_landing.load_signin_screen()
    expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)

    expect(android_sign_in.sign_in_email_label).to_have(values.EMAIL_OR_USERNAME)
    expect(android_sign_in.sign_in_tf_email).to_be_clickable()
    assert android_sign_in.sign_in_tf_email.send_keys(global_contents.login_user_name)

    expect(android_sign_in.sign_in_password_label).to_have(values.PASSWORD)
    expect(android_sign_in.sign_in_password_field).to_be_clickable()
    assert android_sign_in.sign_in_password_field.send_keys(global_contents.login_password)
    expect(android_sign_in.signin_button).to_be_clickable()
    assert android_sign_in.signin_button.click()
    setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")
    if global_contents.whats_new_enable:
        assert whats_new_page.get_close_button.click()
    learn_tab = main_dashboard_page.learn_tab
    expect(learn_tab).to_have(values.MAIN_DASHBOARD_LEARN_TAB, ElementAttribute.CONTENT_DESC)
    expect(learn_tab).to_be_selected()

    yield set_capabilities

    profile_tab = main_dashboard_page.profile_tab
    assert profile_tab.click()
    assert profile_page.settings_button.click()
    profile_page.get_profile_txt_terms_of_use.scroll_vertically_from_element()

    assert profile_page.profile_txt_logout.click()
    expect(profile_page.logout_prompt_logout_button_text).to_have(values.PROFILE_LOGOUT_BUTTON)
    assert profile_page.logout_prompt_logout_button_text.click()
    expect(android_landing.get_search_label).to_have(values.LANDING_SEARCH_TITLE)


@pytest.fixture(scope="module")
def ios_login(set_capabilities, setup_logging):
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
    ios_landing = IosLanding(set_capabilities, setup_logging)
    ios_login = IosLogin(set_capabilities, setup_logging)
    whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
    main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

    log.info("Login screen successfully loaded")
    if ios_landing.get_allow_notifications_button():
        ios_landing.get_allow_notifications_button().click()

    sign_in_button = ios_landing.get_sign_in_button()
    assert sign_in_button.text == values.LOGIN
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
    assert password_field.get_attribute("value") == values.PASSWORD
    password_field.send_keys(global_contents.login_password)
    password_title.click()
    sign_in_button = ios_login.get_signin_button()
    assert sign_in_button.text == values.LOGIN
    sign_in_button.click()
    setup_logging.info(f"{global_contents.login_user_name} is successfully logged in")

    if global_contents.whats_new_enable:
        whats_new_page.get_close_button().click()
        setup_logging.info("Whats New screen is successfully loaded")

    profile_tab = main_dashboard.get_main_dashboard_profile_tab()
    assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
    profile_tab.click()
    learn_tab = main_dashboard.get_main_dashboard_learn_tab()
    learn_tab.click()
    learn_tab = main_dashboard.get_main_dashboard_learn_tab()
    assert learn_tab.get_attribute("value") == values.IOS_SELECTED_TAB_VALUE

    yield set_capabilities

    ios_profile = IosProfile(set_capabilities, setup_logging)
    ios_landing = IosLanding(set_capabilities, setup_logging)
    main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

    profile_tab = main_dashboard.get_main_dashboard_profile_tab()
    profile_tab.click()
    ios_profile.get_profile_settings_button().click()
    ios_profile.get_profile_logout_button().click()
    setup_logging.info("clicking log out")
    ios_profile.get_logout_button().click()
    setup_logging.info("log out successful")
    assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE


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
