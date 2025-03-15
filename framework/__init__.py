from typing import Optional
from .element import Element
from .custom_assertions import CustomAssertions

class Expect:
    def __init__(self):
        self._timeout = 10000

    def __call__(self, locator: Element, message: Optional[str] = None) -> CustomAssertions:
        return CustomAssertions(locator, self._timeout, message=message)


expect = Expect()

__all__ = [
    "Element",
    "expect"
]