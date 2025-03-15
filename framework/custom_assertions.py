import re
from typing import Any, Optional, Union
from framework.element import Element
from tests.common.enums.attributes import ElementAttribute


class CustomAssertions:
    def __init__(
        self,
        locator: Element,
        timeout: int = None,
        is_not: bool = False,
        message: Optional[str] = None,
    ):
        self._locator = locator
        self._timeout = timeout
        self._is_not = is_not
        self._custom_message = message

    @property
    def to_not(self) -> 'CustomAssertions':
        self._is_not = True
        return self
    
    def to_have(self, expected_value: Union[str, re.Pattern], type: Union[str, ElementAttribute] = ElementAttribute.TEXT):
        """
        Asserts that the element contains the specified text or matches the regex pattern
        """
        actual_value = self._locator.get_attribute(type)
        if isinstance(expected_value, str):
            if self._is_not:
                assert actual_value != expected_value, self._custom_message
            else:
                assert actual_value == expected_value, self._custom_message
        elif isinstance(expected_value, re.Pattern):
            if self._is_not:
                assert not re.search(expected_value, actual_value), self._custom_message
            else:
                assert re.search(expected_value, actual_value), self._custom_message

    def to_contain(self, expected_value: str, type: ElementAttribute = ElementAttribute.TEXT):
        """
        Asserts that the element contains the specified text
        """
        if self._is_not:
            assert expected_value not in self._locator.get_attribute(type), self._custom_message
        else:
            assert expected_value in self._locator.get_attribute(type), self._custom_message

    def to_be_selected(self):
        """
        Asserts that the element is selected
        """
        if self._is_not:
            assert not self._locator.is_selected(), self._custom_message
        else:
            assert self._locator.is_selected(), self._custom_message

    def to_be_clickable(self):
        """
        Asserts that the element is clickable
        """
        if self._is_not:
            assert not self._locator.is_clickable(), self._custom_message
        else:
            assert self._locator.is_clickable(), self._custom_message

    def to_be_enabled(self):
        """
        Asserts that the element is enabled
        """
        if self._is_not:
            assert not self._locator.is_enabled(), self._custom_message
        else:
            assert self._locator.is_enabled(), self._custom_message
    
    def to_be_displayed(self):
        """
        Asserts that the element is displayed
        """
        if self._is_not:
            assert not self._locator.is_displayed(), self._custom_message
        else:
            assert self._locator.is_displayed(), self._custom_message