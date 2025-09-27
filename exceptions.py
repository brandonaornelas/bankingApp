class InvalidAmountError(Exception):     
    """Raised when an invalid amount is provided."""
    pass

class InsufficientFundsError(Exception):
    """Raised when there are insufficient funds for a transaction."""
    pass

class OverdraftLimitExceededError(Exception):
    """Raised when a withdrawal exceeds the overdraft limit."""
    pass
