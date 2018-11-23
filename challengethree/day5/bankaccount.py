class BankAccount:
    def __init__(self, account_holder, ):
         self.balance = 0
        self.account_holder = account_holder

    def get_balance(self):
        pass

    def open(self):
        pass

#increases the balance by adding the topped up amount and returns new amount
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

#decreases the amount and returns the current amount after deduction
    def withdraw(self, amount):
        if amount > self.balance:
            return 'sorry your account has less amount.'
        self.balance = self.balance - amount
        return self.balance

    def close(self):
