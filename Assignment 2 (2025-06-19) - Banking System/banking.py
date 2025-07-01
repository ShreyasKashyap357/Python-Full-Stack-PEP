class BankAccount:
    total_accounts = 0  # Class variable to keep track of total accounts created
    def __init__(self, owner:str, balance:float=0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1
    def deposit(self, amt:float):
        if amt > 0:
            self.__balance += amt
            return f"Deposited {amt}. New balance is {self.__balance}."
        else:
            raise ValueError("Deposit amount must be positive.")
    def withdraw(self, amt:float):
        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amt > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amt
    @property
    def balance(self) -> float:
        return self.__balance
    @balance.setter
    def balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance must be non-negative.")
    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.__balance!r})"
    def __add__(self, other): 
        if not isinstance(other, BankAccount):
            return NotImplemented
        BankAccount.total_accounts -= 1
        new_owner = f"{self.owner} {other.owner}"
        return BankAccount(new_owner, self.__balance + other.__balance)

class SavingsAccount(BankAccount):
    def __init__(self, owner:str, balance:float=0.0, interest_rate:float=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return f"Applied interest: {interest}. New balance is {self.balance}."

class CheckingAccount(BankAccount):
    def __init__(self, owner:str, balance:float=0.0, overdraft_limit:float=0.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit if overdraft_limit >= 0 else 0.0
    def withdraw(self, amt:float):
        if amt <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amt > self.balance + self._overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance = self.balance - amt
    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit
    @overdraft_limit.setter
    def overdraft_limit(self, limit: float):
        if limit >= 0:
            self._overdraft_limit = limit
        else:
            raise ValueError("Overdraft limit must be non-negative.")

class Customer:
    def __init__(self, name:str):
        self.name = name
        self.accounts = []
    def add_account(self, account:BankAccount):
        if isinstance(account, BankAccount):
            self.accounts.append(account)
            return f"Account added for {self.name}."
        else:
            raise ValueError("Only BankAccount instances can be added.")
    def total_balance(self) -> float:
        return sum(account.balance for account in self.accounts)
    def transfer(self, from_account:BankAccount, to_account:BankAccount, amt:float):
        if from_account not in self.accounts or to_account not in self.accounts:
            raise ValueError("Both accounts must belong to the customer.")
        try:
            from_account.withdraw(amt)
            to_account.deposit(amt)
        except ValueError as e:
            print(f"Transfer failed: {e}")
    def __str__(self):
        return f"Customer(name={self.name}, accounts={len(self.accounts)}, total_balance={self.total_balance()})"
    def __repr__(self):
        return f"Customer(name={self.name!r}, accounts={self.accounts!r})"

def print_account_summary(obj):
    try:
        owner = obj.owner
        try:
            balance = obj.balance
        except AttributeError:
            balance = obj.get_balance()
        print(f"Account Owner: {owner}, Balance: {balance}")
    except AttributeError as e:
        print(f"Error: {e}. The object does not have the required attributes.")

def demo_polymorphism():
    accounts = [
        SavingsAccount("Alice", 1000, 0.03),
        CheckingAccount("Bob", 500, 200)
    ]
    for account in accounts:
        print_account_summary(account)
        try:
            print(account.deposit(250))
            print(f"Balance after depositing 250: {account.balance}")
            print(account.withdraw(600))
            print(f"Balance after withdrawing 600: {account.balance}")
        except ValueError as e:
            print(f"Operation failed: {e}")
        if hasattr(account, 'interest_rate'):
            print(account.apply_interest())
    try:
        merged_account = accounts[0] + accounts[1]
        print("\nMerged Account:")
        print_account_summary(merged_account)
    except TypeError as e:
        print(f"Error merging accounts: {e}")
