class BaseAppException(Exception):
    """Base exception class for all application-specific exceptions."""

    def __init__(self, message: str, details: str = ""):
        self.message = message
        self.details = details
        super().__init__(self.message)


class GiftError(BaseAppException):
    """Base exception for gift-related errors."""


class GiftsRetrievalError(GiftError):
    """Exception levée lors d'erreurs de récupération des cadeaux."""


class GiftUserError(BaseAppException):
    """Base exception for gift_user related errors."""


class GiftsUserRetrievalError(GiftError):
    """Exception levée lors d'erreurs de récupération des gift_users"""
