# Add these attributes and behaviors to the class Account
# Add attributes deposits and withdrawals in the init method 
# which are empty lists by default and another attribute loan_balance
#  which is zero by default.
class Account:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    # Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance

    # Update the deposit method to append each deposit transaction 
    # to the deposits list. Each transaction should be in form 
    # of a dictionary like this  
    # {
    #    "amount": amount,
    #    "narration": "deposit"
    # }
    def deposit(self, amount):
        self.balance += amount
        deposit_transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(deposit_transaction)
        return f"You have deposited ksh {amount} and your total amount is {deposit_transaction}"

# Update the withdrawal method to append eachd
#  withdrawal transaction to the withdrawals list.
#  Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.withdrawals = []

    def withdrawal(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            withdrawal_transaction = {
                "amount": amount,
                "narration": "withdrawal"
            }
            self.withdrawals.append(withdrawal_transaction)
        return f"You have withdrawn {withdrawal_transaction} and your balance is {amount}"

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the account balance

class Customer:
    def __init__(self, name, balance, loan_balance):
        self.name = name
        self.balance = balance
        self.loan_balance = loan_balance

    def repay_loan(self, amount):
        if amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.balance += overpayment
            return "Loan fully repaid"
        else:
            self.loan_balance -= amount
            self.balance += amount
            return "Loan partially repaid"
print(f"You have paid a loan of {Customer.repay_loan} and you have a balance of {BankAccount}")

# Add a transfer method which accepts
#  two attributes (amount and instance of another account). 
# If the amount is less than the current ins
# tances balance, the method transfers the requested amount from 
# the current account to the passed account. The transfer is 
# accomplished by reducing the current account balance
#  and depositing the requested amount to the passed account.
    
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
        else:
            return "Insufficient funds for transfer"

        return "Transfer successful"
    print(f"You've transfered {deposit} and you have {Account.check_balance} as your balance")