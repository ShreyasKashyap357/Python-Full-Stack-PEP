from banking import BankAccount, SavingsAccount, CheckingAccount, Customer, print_account_summary

class CryptoWallet:
    def __init__(self, owner: str, amount: float = 0.0):
        self.owner = owner
        self._amount = amount
    def get_balance(self):
        return self._amount
    def add_funds(self, amount: float):
        if amount > 0:
            self._amount += amount
        else:
            raise ValueError("Amount must be positive")

def main():
    # Create and manipulate BankAccount instances
    account1 = BankAccount("Alice", 1000.0)
    account2 = BankAccount("Bob", 500.0)
    try:
        account1.deposit(200.0)
        print(f"Account1 after depositing 200: {account1.balance}")
        account1.withdraw(150.0)
        print(f"Account1 after withdrawing 150: {account1.balance}")
        account2.deposit(300.0)
        print(f"Account2 after depositing 300: {account2.balance}")
        account2.withdraw(100.0)
        print(f"Account2 after withdrawing 100: {account2.balance}")
    except ValueError as e:
        print(f"Error: {e}")
    # Create SavingsAccount and CheckingAccount
    savings_account = SavingsAccount("Charlie", 1500.0, 0.05)
    checking_account = CheckingAccount("David", 800.0, 200.0)
    try:
        savings_account.deposit(100.0)
        print(f"Savings after depositing 100: {savings_account.balance}")
        savings_account.withdraw(200.0)
        print(f"Savings after withdrawing 200: {savings_account.balance}")
        print(savings_account.apply_interest())
        checking_account.deposit(50.0)
        print(f"Checking after depositing 50: {checking_account.balance}")
        checking_account.withdraw(900.0)
        print(f"Checking after withdrawing 900 (overdraft): {checking_account.balance}")
        checking_account.withdraw(100.0)
        print(f"Checking after withdrawing 100: {checking_account.balance}")
    except ValueError as e:
        print(f"Error: {e}")
    # Merge accounts
    try:
        merged_account = savings_account + checking_account
        print(f"Merged Account Balance: {merged_account.balance}")
        print_account_summary(merged_account)
    except TypeError as e:
        print(f"Error merging accounts: {e}")
    # Create Customer and add accounts
    customer = Customer("Eve")
    customer.add_account(savings_account)
    customer.add_account(checking_account)
    print(f"Total balance for {customer.name}: {customer.total_balance()}")
    try:
        customer.transfer(savings_account, checking_account, 200.0)
        print(f"After transfer: Savings - {savings_account.balance}, Checking - {checking_account.balance}")
    except ValueError as e:
        print(f"Transfer error: {e}")
    # Duck typing demo with CryptoWallet
    crypto_wallet = CryptoWallet("Frank", 1000.0)
    print("\nDuck Typing Demo:")
    print_account_summary(savings_account)
    print_account_summary(crypto_wallet)
    # Print all objects
    print("\nObject Representations:")
    print(f"BankAccount1: {account1}")
    print(f"BankAccount1 repr: {repr(account1)}")
    print(f"BankAccount2: {account2}")
    print(f"BankAccount2 repr: {repr(account2)}")
    print(f"SavingsAccount: {savings_account}")
    print(f"SavingsAccount repr: {repr(savings_account)}")
    print(f"CheckingAccount: {checking_account}")
    print(f"CheckingAccount repr: {repr(checking_account)}")
    print(f"Customer: {customer}")
    print(f"Customer repr: {repr(customer)}")
    print(f"CryptoWallet: {crypto_wallet}")
    print(f"CryptoWallet repr: {repr(crypto_wallet)}")
    # Print total accounts
    print(f"\nTotal bank accounts created: {BankAccount.total_accounts}")

if __name__ == "__main__":
    main()
