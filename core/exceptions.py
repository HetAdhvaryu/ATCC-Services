class ProfileError(Exception):
    """Base class for profile-related errors"""


class ProfileValidationError(ProfileError):
    """Raised when a font profile fails validation"""


class RuleNotFoundError(ProfileError):
    """Raised when a referenced rule does not exist"""


class ProfileNotFoundError(ProfileError):
    """Raised when profile file is missing"""
