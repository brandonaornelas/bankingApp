from exceptions import InvalidAmountError, InsufficientFundsError, OverdraftLimitExceededError


class BankAccount:

    def __init__(self, balance=0):
        self.__balance = float(balance)
    
    def _require_positive_amount(self, amount):  # Helper method to validate positive amounts
        try:
            amt = float(amount)
        except Exception:
            raise InvalidAmountError("Amount must be a number")
        if amt <= 0:
            raise InvalidAmountError("Amount must be positive")
        return amt
    
    def deposit(self, amount):
        amt = self._require_positive_amount(amount)
        self.__balance += amt
    
    def withdraw(self, amount):
        amt =- self._require_positive_amount(amount)
        if amt > self.__balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.__balance -= amt
    
    def transfer_to(self, other, amount):
        amt = self._require_positive_amount(amount)
        if amt > self.__balance:
            raise InsufficientFundsError("Insufficient funds for transfer")
        self.withdraw(amt)
        other.deposit(amt)

    @property # Read-only property
    def balance(self):
        return self.__balance

class SavingsAccount(BankAccount):

    def add_interest(self, rate):
        r = self._require_positive_amount(rate)
        self.deposit(self.balance * r)
    
    def withdraw(self, amount):
        amt = self._require_positive_amount(amount)
        if amt > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        super().withdraw(amt)

class CheckingAccount(BankAccount):
    def __init__(self, balance=0, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        amt = self._require_positive_amount(amount)
        new_balance = self.balance - amt
        if new_balance < -self.overdraft_limit:
            raise OverdraftLimitExceededError("Withdrawal exceeds overdraft limit")
        self._BankAccount__balance = new_balance  # Directly modify the private balance

if __name__ == "__main__":
    """
    # Quick demo showing exception handling
    s = SavingsAccount(100)
    c = CheckingAccount(50, overdraft_limit=100)


    try:
        s.deposit(25)
        s.withdraw(200) # will raise InsufficientFunds
    except InsufficientFundsError as e:
        print("Savings error:", e)


    try:
        c.withdraw(120) # allowed: 50 - 120 = -70 (within -100)
        c.withdraw(50) # will raise OverdraftExceeded: -70 - 50 = -120
    except OverdraftLimitExceededError as e:
        print("Checking error:", e)


    try:
        s.transfer_to(c, -10) # will raise InvalidAmount
    except InvalidAmountError as e:
        print("Transfer error:", e)


    print("Savings balance:", s.balance)
    print("Checking balance:", c.balance)
    """
    acc = BankAccount(200)
    print(acc.balance)

    acc.deposit(50)
    print(acc.balance)

    acc.withdraw(30)
    print(acc.balance)