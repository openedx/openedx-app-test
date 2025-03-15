"""
User Defined Exceptions
"""


from tests.common import values


class NotFoundError(Exception):
    """Element not Found within the given time span"""

    pass


class UnwantedElementPresence(Exception):
    """An Element that should not be Visible is Found"""

    pass


class InvalidElementState(Exception):
    """Element is not in the Expected State e.g checkbox is not checked"""

    pass


class ElementInteractionError(Exception):
    """Interaction with element like send_keys or click failed"""

    pass


class ElementNotInList(Exception):
    """An Item was not found in the list of Items"""

    pass


class EnvironmentalError(Exception):
    """An Error occurred while setting up the testing environment"""

    pass


class VerificationError(Exception):
    """Comparison Between Some Values Failed"""

    @staticmethod
    def of(failed_on, expected, actual):
        return VerificationError(values.VERIFICATION_FAILED_ERROR.format(failed_on, expected, actual))