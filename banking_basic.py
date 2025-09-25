class BankAccount:

    def __init__(self, balance=0):
        self.__balance = float(balance)
    
    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount")
            return
        self.__balance += amount
    
    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.__balance:
            print("Insufficient funds")
            return
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    @property
    def balance(self):
        return self.__balance
    
    def transfer_to(self, other, amount):
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.__balance:
            print("Insufficient funds")
        self.__balance -= amount
        other.deposit(amount)

class SavingsAccount(BankAccount):

    def add_interest(self, rate):
        rate = float(rate)
        if rate <= 0:
            print("Invalid rate")
            return
        self.deposit(self.get_balance() * rate)
    
    def withdraw(self, amount):
        amoutn = float(amount)
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, balance=0, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Invalid amount")
            return
        new_balance = self.balance - amount
        if new_balance < -self.overdraft_limit:
            print("Overdraft limit exceeded")
            return
        self._BankAccount__balance = new_balance


if __name__ == "__main__":
    s = SavingsAccount(1000)
    c = CheckingAccount(100, overdraft_limit=200)


    s.add_interest(0.02)
    s.withdraw(50)


    c.withdraw(250)
    c.withdraw(100)


    s.transfer_to(c, 200)


    print("Savings:", s.balance)
    print("Checking:", c.balance)