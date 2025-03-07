import os
import logging
from datetime import datetime, timezone
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
