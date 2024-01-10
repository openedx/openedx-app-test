"""
   Module covers iOS base page
"""

from tests.common.globals import Globals


class IosBasePage:
    """
    Base page for all iOS Pages
    """

    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.global_contents = Globals(setup_logging)
        self.log = setup_logging
