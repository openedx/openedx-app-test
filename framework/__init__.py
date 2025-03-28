from typing import Optional

from .custom_assertions import CustomAssertions
from .element import Element


class Expect:
    def __init__(self):
        self._timeout = 10000

    def __call__(
        self, locator: Element, message: Optional[str] = None
    ) -> CustomAssertions:
        return CustomAssertions(locator, self._timeout, message=message)


expect = Expect()

__all__ = ["Element", "expect"]
