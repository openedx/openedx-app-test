"""utils module"""

import logging
import os
import random
import string
from datetime import datetime, timezone
from unicodedata import normalize

logger = logging.getLogger(__name__)


def create_directory(target_directory):
    """
    Create directory by specific given name

    Argument:
        target_directory (str): directory name to create
    """
    try:
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
    except OSError as os_error:
        logger.warning(os_error)


def sanitize_name(name):
    return name.replace(",", "_").replace(" ", "")


def get_formatted_datetime():
    """
    Get a string from current datetime in year, month, day, hour, min & sec format
    Returns:
        str : i.e. 2020_01_08_12_51
    """

    return datetime.now(timezone.utc).strftime("%Y_%m_%d_%I_%M")


def generate_random_credentials(length):
    """
    Generate random alphanumeric strings

    Arguments:
        length (int): length of string to generate

    Return:
        str: random string
    """

    combination = string.ascii_lowercase + string.digits
    return "".join(random.choice(combination) for _ in range(length))


def normalize_string(text, form="NFC"):
    """
        Normalize Unicode Strings in Composed Form to accurately match text in Locales
    Arguments:
        text (str) : Unicode String to Normalize
        form (str): Valid values for form are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’
    Returns:
        str : Normalized Form Composed (NFC) Version of UTF-8
    """
    return normalize(form, text)


def save_page_source_to_file(driver, filename="page_source.xml"):
    """
    Saves the current page source from the Appium driver to a specified file.

    Args:
        driver: The Appium WebDriver instance.
        filename (str): The name of the file to save the page source to.
                        Defaults to "page_source12.xml".
    """
    try:
        page_source = driver.page_source
        with open(filename, "w", encoding="utf-8") as f:
            f.write(page_source)
        print(f"Page source successfully saved to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Error saving page source to file {filename}: {e}")
