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


class CountryAbbreviation(Enum):
    """CountryAbbreviation"""

    US = "us"
    CA = "ca"


class LanguageAbbreviation(Enum):
    """CountryAbbreviation"""

    EN = "en"
    FR = "fr"


class GenderOptions(Enum):
    """Gender Options"""

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other/Prefer Not to Say"


class EducationLevel(Enum):
    """Education level"""

    DOCTORATE = "Doctorate"
    MASTER_OR_PROFESSIONAL_DEGREE = "Master's or professional degree"
    BACHELOR = "Bachelor's degree"
    ASSOCIATE = "Associate degree"
    SECONDARY = "Secondary/high school"
    JUNIOR_TO_MIDDLE = "Junior secondary/junior high/middle school"
    NO_FORMAL_EDUCATION = "No formal education"
    OTHER = "Other education"


class Country(Enum):
    """Country Name"""

    CANADA = "Canada"
    USA = "United States of America"


class Language(Enum):
    """Languages"""

    ENGLISH = "English"
    FRENCH = "French"


class Subjects(Enum):
    """Subjects"""

    COMPUTER_SCIENCE = "Computer Science"
    DATA_SCIENCE = "Data Science"
    ENGINEERING = "Engineering"
    MATH = "Math"
    BUSINESS = "Business"
    ART = "Art"
    HISTORY = "History"
    LANGUAGE = "Language"
    SCIENCE = "Science"
    SOCIAL_SCIENCE = "Social Science"
    HEALTH = "Health"
    OTHER = "Other"


class DiscoverSections(Enum):
    """Discover Sections"""

    MOST_POPULAR = "Most popular"
    EXECUTIVE_EDUCATION = "Executive Education"
    MASTER_DEGREE = "Master’s Degrees"
    BACHELOR_DEGREE = "Bachelor’s Degrees"
    NEW = "New"
    TRENDING = "Trending"


class AppContext(Enum):
    """App Context"""

    NATIVE = "NATIVE_APP"
    WEBVIEW = "WEBVIEW"
