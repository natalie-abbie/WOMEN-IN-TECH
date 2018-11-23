class BankAccount:
    
    def __init__(self, account_holder,password):
         self.balance = 0
        self.account_holder = account_holder
        self.password = password
        
#user functions that the user of the account will need when accessing the account
    def user_function(self):
        print("For any action on your account: ")
        print ("press any key as below:" + "\n"
             + "B: Check Balance" + "\n"
             + "D: Deposit cash" + "\n"
             + "W: Withdraw cash" + "\n"
             + "X: Delete account " + "\n"
             + "E: Exit service" + "\n")

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
        pass
