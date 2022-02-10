# Create a file with the User class, including the __init__ and make_deposit methods
class User:		# here's what we have so far
    account_balance = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
# Add a make_withdrawal method to the User class
    def make_withdrawl(self,amount):
        self.account_balance-= amount
        return self
# Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(self.account_balance)
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
    def transfer_money(self,amount,other_user):
        self.account_balance-=amount
        other_user.account_balance+=amount

# Create 3 instances of the User class
User1=User('Brandon','Brandonb152@gmail.com')
User2=User('Luna','Luna@gmail.com')
User3=User('Tom','Tom@gmail.com')

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
User1.make_deposit(500000000).make_deposit(100000000).make_withdrawl(20000).display_user_balance()
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
User2.make_deposit(90000000).make_deposit(1000000).make_withdrawl(20000).make_withdrawl(20000).display_user_balance()
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
User3.make_deposit(1000).make_withdrawl(2000).make_withdrawl(2000).make_withdrawl(1000).display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
User1.transfer_money(5000,User3)
User1.display_user_balance()
User3.display_user_balance()
