# Create a class BankAccount with attributes account_holder and balance.
# Add methods:

# deposit(amount)

# withdraw(amount)

# show_balance()

class BankAccount:
    def __init__(self,account_holder,balance = 0):
       self.account_holder = account_holder
       self.balance = balance
       
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}.")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("insuffient balance")
        else: 
            self.balance -= amount
            print(f"{amount} withdrawed. New balance is {self.balance}.")
            
    def show_balance(self):
         print(f"Account holder: {self.account_holder}, Balance: {self.balance}")
         
         
# Create an account
acc1 = BankAccount("John Doe", 1000)

# Perform some operations
acc1.show_balance()
acc1.deposit(2545000)
acc1.withdraw(11200)
acc1.withdraw(155500)  # should show insufficient balance
acc1.show_balance()