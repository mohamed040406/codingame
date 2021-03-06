class CodinGameAPIError(Exception):
    """Base exception for the CodinGame API."""
    def __init__(self, message: str):
        self.message = message

class CodinGamerNotFound(CodinGameAPIError):
    """Raised when a CodinGamer isn't found."""
    pass
