"""
This module defines the CustomAssertions class which provides custom assertions for the Element class.
"""

import re
from typing import Optional, Union
from framework.element import Element
from tests.common.enums.attributes import ElementAttribute


class CustomAssertions:
    """
    A class containing custom assertions for the Element class.
    The methods in this class provide a convenient way to perform assertions
    on an Element instance. The assertions are provided as methods to allow
    for more readable tests.
    Example:
        element = Element("accessibility_id", "Element")
        expect(element).to_be_visible()
    """

    def __init__(
        self,
        locator: Element,
        timeout: int = None,
        is_not: bool = False,
        message: Optional[str] = None,
    ):
        """
        Initializes a CustomAssertions instance.

        Args:
            locator (Element): The element to be asserted.
            timeout (int, optional): The maximum time to wait for the assertion. Defaults to None.
            is_not (bool, optional): Negates the assertion if True. Defaults to False.
            message (Optional[str], optional): Custom message for the assertion. Defaults to None.
        """
        # Store the element to be asserted
        self._locator = locator

        # Set the timeout for the assertion
        self._timeout = timeout

        # Flag to indicate if the assertion is negated
        self._is_not = is_not
        self._custom_message = message

    @property
    def not_(self) -> "CustomAssertions":
        """
        Negates the assertion

        Using this property will invert the boolean value of the assertion.
        This is useful when you want to assert that an element does not contain a
        certain text or does not have a certain attribute.

        For example, if you want to assert that an element does not have the
        text "Hello World", you can use the following code:

        expect(element).not_.to_have("Hello World")

        This will pass if the element does not have the text "Hello World",
        and fail if the element does have the text "Hello World".

        This property is useful when you want to assert that an element does not
        have a certain attribute or property.

        For example, if you want to assert that an element does not have the
        attribute "disabled", you can use the following code:

        expect(element).not_.to_have("disabled")

        This will pass if the element does not have the attribute "disabled",
        and fail if the element does have the attribute "disabled".

        This property can be used with any of the assertion methods, such as
        `to_have`, `to_contain`, `to_be_visible`, etc.
        """
        self._is_not = True
        return self

    def to_have(
        self,
        expected_value: str,
        attribute: Union[str, ElementAttribute] = ElementAttribute.TEXT,
        case: Optional[str] = None,
    ):
        """Asserts that the element matches the specified text

        Args:
            expected_value (str): The text or to compare with the element's attribute.
            attribute (Union[str, ElementAttribute], optional): The attribute to retrieve from the element.
                Defaults to TEXT.
            case (Optional[str], optional): The case to compare the values. Can be 'lower' or 'upper'. Defaults to None.
        """
        actual_value = self._locator.get_attribute(attribute)

        if case:
            actual_value = actual_value.lower() if case == "lower" else actual_value.upper()

        default_msg = f'Expected "{expected_value}" but found "{actual_value}"'
        custom_msg = self._custom_message or default_msg
        match_result = expected_value == actual_value
        assert match_result != self._is_not, custom_msg

    def to_match(
        self,
        pattern: re.Pattern,
        attribute: ElementAttribute = ElementAttribute.TEXT,
        partial: bool = False,
    ):
        """Asserts that the element's attribute matches the specified regex pattern.

        Args:
            pattern (re.Pattern): The regex pattern to match against the element's attribute.
            attribute (ElementAttribute, optional): The attribute to retrieve from the element. Defaults to TEXT.
            partial (bool, optional): If True, performs a partial match (using re.search).
                                    If False, performs a full match (using re.fullmatch). Defaults to False.
        """
        actual_value = self._locator.get_attribute(attribute)
        # TODO: modify for negative scenario
        default_msg = f'Expected pattern "{pattern}" to {"partially" if partial else "fully"} match "{actual_value}"'
        custom_msg = self._custom_message or default_msg
        match_func = re.search if partial else re.fullmatch
        match_result = match_func(pattern, actual_value)
        assert match_result != self._is_not, custom_msg

    def to_contain(
        self,
        expected_value: str,
        attribute: ElementAttribute = ElementAttribute.TEXT,
        case: Optional[str] = None,
    ):
        """Asserts that the element contains the specified text.

        Args:
            expected_value (str): The text to compare with the element's attribute.
            attribute (ElementAttribute, optional): The attribute to retrieve from the element. Defaults to TEXT.
            case (Optional[str], optional): The case to compare the values. Can be 'lower' or 'upper'. Defaults to None.
        """
        actual_value = self._locator.get_attribute(attribute)
        if case:
            actual_value = actual_value.lower() if case == "lower" else actual_value.upper()
        # TODO: modify for negative scenario
        default_msg = f'Expected "{actual_value}" to contain "{expected_value}"'
        custom_msg = self._custom_message or default_msg
        match_result = expected_value in actual_value
        assert match_result != self._is_not, custom_msg

    def to_be_selected(self):
        """Asserts that the element is selected

        This assertion is useful for verifying checkboxes, radio buttons,
        and options in a select element. The assertion works by checking
        the selected property of the element.

        Raises:
            AssertionError: If the element is not selected and the assertion
                is not negated (i.e., `to_not` is not used).
        """

        if self._is_not:
            assert not self._locator.is_selected(), self._custom_message
        else:
            assert self._locator.is_selected(), self._custom_message

    def to_be_clickable(self):
        """Asserts that the element is clickable

        This assertion is useful for verifying whether an element is clickable.
        An element is considered clickable if it is visible and enabled.
        """
        if self._is_not:
            assert not self._locator.is_clickable(), self._custom_message
        else:
            assert self._locator.is_clickable(), self._custom_message

    def to_be_enabled(self):
        """Asserts that the element is enabled

        An element is considered enabled if it is visible and can be interacted with.
        """
        if self._is_not:
            assert not self._locator.is_enabled(), self._custom_message
        else:
            assert self._locator.is_enabled(), self._custom_message

    def to_be_visible(self):
        """
        Asserts that the element is enabled
        """
        if self._is_not:
            assert not self._locator.get_attribute(ElementAttribute.VISIBLE), self._custom_message
        else:
            assert self._locator.get_attribute(ElementAttribute.VISIBLE), self._custom_message

    def to_be_displayed(self):
        """
        Asserts that the element is displayed.

        An element is considered displayed if it is visible and has a height
        and width greater than 0.
        """
        if self._is_not:
            assert not self._locator.is_displayed(), self._custom_message
        else:
            assert self._locator.is_displayed(), self._custom_message

    def to_be_checked(self):
        """Asserts that the element is selected
        This assertion is useful for verifying checkboxes, radio buttons,
        and options in a select element. The assertion works by checking
        the selected property of the element.
        Raises:
            AssertionError: If the element is not selected and the assertion
                is not negated (i.e., `to_not` is not used).
        """

        if self._is_not:
            assert not self._locator.is_checked(), self._custom_message
        else:
            assert self._locator.is_checked(), self._custom_message
