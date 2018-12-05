class BankAccount():
    def __init__(self, account_number, name, pin_number):
        self.status = "open"
        self.account_number = account_number
        self.name = name
        self.pin_number = pin_number

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
        if self.status != "open":
            raise ValueError
        return self.balance

    def open(self, balance = 0):
        self.balance = balance
        return self.balance 

    def deposit(self, amount):
        if self.status == "closed":
            raise ValueError
        if amount <=0:
            raise ValueError

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError
        
        if amount < 0:
            raise ValueError
        
        self.balance -= amount
        return self.balance

    def close(self):
        #close account 
        self.status = "closed"
        return self.status
