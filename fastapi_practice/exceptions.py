"""Custom exceptions."""


class StoryException(Exception):
    """Exception when story is detected."""

    def __init__(self, name: str) -> None:
        """Init StoryException instance."""
        self.name = name
