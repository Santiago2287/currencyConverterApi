class CurrencyNetworkError(Exception):
    """Exception for network errors or external server outages."""
    pass

class CurrencyDataError(Exception):
    """Exception for when the API responds with an unexpected format."""
    pass