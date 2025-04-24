"""Expect Module

This module contains an Expect class which is used to create custom assertions
over the Element class. It allows the creation of custom assertion methods that
are not natively supported by the Element class.

The Expect class is used to create custom assertions over the Element class.
It allows the creation of custom assertion methods that are not natively
supported by the Element class.

The Expect class is used in the following way:

    expect(element).to_have("text")

    expect(element).not_.to_have("text")

    expect(element).to_have("text", timeout=1000)

    expect(element).not_.to_have("text", timeout=1000)

"""

from typing import Optional

from .custom_assertions import CustomAssertions
from .element import Element


class Expect:
    """The Expect class is used to create custom assertions over the Element class.

    It allows the creation of custom assertion methods that are not natively
    supported by the Element class. The Expect class provides a fluent interface
    for creating assertions on web elements, enabling more readable and
    maintainable test code.
    """

    def __init__(self):
        pass

    def __call__(self, locator: Element, message: Optional[str] = None, timeout: int = 10000) -> CustomAssertions:
        return CustomAssertions(locator, timeout, message=message)


expect = Expect()

__all__ = ["Element", "expect"]
