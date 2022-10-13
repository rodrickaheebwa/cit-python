# Aheebwa Rodrick
# Quiz on classes

class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def transact(self, transaction):
        if transaction.type == "deposit":
            self.balance += transaction.amount
        elif transaction.type == "withdraw":
            self.balance -= transaction.amount

    def __str__(self) -> str:
        return f"\n Account number: {self.account_number}\n Account owner: {self.owner}\n Account balance: {self.balance}\n Account type: {self.type}"

class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self) -> str:
        return f"Bank name: {self.name}"

class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self) -> str:
        return f"Customer name: {self.name}"

class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type
        self.transactions = []

    def __str__(self) -> str:
        return f"\nA {self.type} transaction of {self.amount} has been made on the account {self.account.account_number} in the names of {self.account.owner}\n Balance is: {self.account.balance}"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

# creating new bank, customer and account objects
bank = Bank("RIKO", [])
customer = Customer("Rodrick", [])
bank_account = BankAccount(3200245784, 5000.0, "Rodrick", "personal")

# adding new account to bank and customer
bank.add_account(bank_account)
customer.add_account(bank_account)

print(bank)
print(customer)
print(bank_account)

# creating a new transaction and adding it to the account
transaction = Transactions(bank_account, 1000.0, "withdraw")
bank_account.transact(transaction)
transaction.add_transaction(transaction)

# new output after transaction
print(transaction)
print(bank_account)