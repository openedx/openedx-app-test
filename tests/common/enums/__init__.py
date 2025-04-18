"""
This module aggregates and exports essential enumerations used across the codebase,
such as attributes and platform-specific views.
"""

from .attributes import ElementAttribute
from .general_enums import ScrollDirections, TargetPlatform, IosClassViews

__all__ = ["ElementAttribute", "ScrollDirections", "IosClassViews", "TargetPlatform"]
