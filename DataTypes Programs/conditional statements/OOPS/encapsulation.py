class BankAccount:
    def __init__(self, balance):  
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def getbalance(self):
        return self.balance

account = BankAccount(1000)

# Perform transactions
account.deposit(500)   
account.withdraw(300)  

print("Current Balance:", account.getbalance())

