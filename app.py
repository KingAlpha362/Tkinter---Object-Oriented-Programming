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
    def get_balance(self):
        return self.balance
        
account = BankAccount(0)
account.deposit(500)
account.withdraw(200)
print("Current Balance:", account.get_balance())
