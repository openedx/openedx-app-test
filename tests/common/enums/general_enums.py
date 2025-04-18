"""
This module contains general enums used across the framework.
"""

from enum import Enum


class ScrollDirections(Enum):
    """Device scroll directions"""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class IosClassViews(Enum):
    """Ios class view"""

    BUTTON = "Button"
    STATIC_TEXT = "StaticText"
    TEXT_FIELD = "TextField"
    TEXT_AREA = "TextView"
    SWITCH = "Switch"
    TABLE = "Table"
    TABLE_CELL = "Cell"


class TargetPlatform(Enum):
    """TargetPlatform"""

    IOS = "iOS"
    ANDROID = "Android"
