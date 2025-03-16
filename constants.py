"""Module defining contants."""

from enum import Enum


class BlogType(str, Enum):
    """Blog types"""

    SHORT = "short"
    STORY = "story"
    HOWTO = "howto"
