class BankAccount:
    Accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.Accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if amount>self.balance:
            print('insufficient funds: Charging a $5 fee')
            self.balance-=5
            return self
        else:
            self.balance-=amount
            return self
    def display_account_info(self):
        print(self.balance) 
    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.int_rate
            return self
        else:
            print('negative balance')
    @classmethod
    def printAccounts(cls):
            print(cls.Accounts)

Account1=BankAccount(.015,90000)
Account2=BankAccount(.01,110000)

Account1.deposit(5000).deposit(5000).deposit(10000).yield_interest().display_account_info()
Account2.deposit(10000).deposit(10000).withdraw(30000).withdraw(50000).withdraw(5000).withdraw(2000).yield_interest().display_account_info()

BankAccount.printAccounts()