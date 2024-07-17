class Account:
    def __init__(self, bank_account, account_owner, balance):
        self.bank_account = bank_account
        self.account_owner = account_owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f'Amount: {amount} added to balance, as of now balance: {self.balance}')
        else:
            print('Deposit should be a positive number')

    def withdraw(self, amount):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            print(f'Amount of money withdrawn: {amount}, as of now balance: {self.balance}')
        else:
            print('Not enough amount in balance or invalid amount')

    def __repr__(self):
        return f'Account({self.bank_account}, {self.account_owner}, {self.balance})'


class Customer:
    def __init__(self, full_name, user_id):
        self.full_name = full_name
        self.user_id = user_id
        self.accounts_list = []

    def add_account(self, account):
        if account in self.accounts_list:
            print('Account already exists')
        else:
            self.accounts_list.append(account)
            print('Account added')

    def __repr__(self):
        return f'Customer({self.full_name}, {self.user_id}, Accounts: {self.accounts_list})'


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers_list = []

    def add_customer(self, customer):
        if customer in self.customers_list:
            print('Customer already exists')
        else:
            self.customers_list.append(customer)
            print(f'{customer} added')

    def transaction(self, from_acc, to_acc, amount):
        if from_acc.balance >= amount:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            print(f'Transferred {amount} from {from_acc.bank_account} to {to_acc.bank_account}')
        else:
            print('Error in transaction: insufficient balance')

    def display_customers(self):
        for customer in self.customers_list:
            print(customer)


client = Customer("Ruz Shawn", "12345S")
c1 = Account("123456", "Ruz Shawn", 1000.0)
c2 = Account("654321", "Ruz Shawn", 500.0)
client.add_account(c1)
client.add_account(c2)
print(client)

bank_name = Bank('mybank')
bank_name.add_customer(client)

c1.deposit(500)
c2.withdraw(300)
bank_name.transaction(c1, c2, 200)
