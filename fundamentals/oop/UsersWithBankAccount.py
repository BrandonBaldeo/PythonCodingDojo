class BankAccount:
    Accounts= []
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.Accounts.append(self)
# Add a deposit method to the BankAccount class
    def deposit(self,amount):
      self.balance+=amount
      return self
# Add a withdraw method to the BankAccount class
    def withdrawl(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
# Add a display_account_info method to the BankAccount class
    def display_account_info(self):
        print(self.balance)
        return self
# Add a yield_interest method to the BankAccount class
    def yield_interest(self):
        if self.balance>0:
         self.balance*self.int_rate+self.balance
        return self


class User:
    amount_of_users=0
    account_list = []

# Update the User class __init__ method
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        User.account_list.append(self)
        User.amount_of_users+=1
# Update the User class make_deposit method
    def make_deposit(self, account_number, amount):
        self.account.balance += amount
        return self
# Update the User class make_withdrawal method
    def make_withdrawl(self, account_number, amount):
        self.account.balance -= amount
        return self
# Update the User class display_user_balance method
    def display_user_balance(self):
        print(self.account.balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.balance += amount
        return self
