"""This module imports and exports enums used across the test framework.

It imports `ElementAttribute` from the `attributes` module and
`ScrollDirections`, `TargetPlatform`, and `IosClassViews` from the `general_enums` module.
These enums are then made available for other modules by including them in the `__all__` list.
"""

from .attributes import ElementAttribute
from .general_enums import ScrollDirections, TargetPlatform, IosClassViews

__all__ = ["ElementAttribute", "ScrollDirections", "IosClassViews", "TargetPlatform"]
