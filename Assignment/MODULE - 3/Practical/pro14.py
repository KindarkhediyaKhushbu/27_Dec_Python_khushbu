#Write a Python program to show multilevel inheritance.

class creat_acc:
    account_no = int
    holder_name = str
    account_type = str
    dep_amount = int
    balance = int
    withdraw_amount = int 

    def account_create(self):
        self.account_no = int(input("Enter the account no:"))
        self.holder_name = input("Enter the holder name:")
        self.account_type = input("Enter the account type:")
        self.balance = int(input("Enter your balance:"))
        print("ACCOUNT CREATED SUCCESSFULLY")

class deposit(creat_acc):
    
    def deposit(self):
        self.dep_amount = int(input("Enter the amount to deposit:"))
        if self.dep_amount >= 2000:
            self.balance += self.dep_amount
            print("Amount deposited")
        else:
            print("Minimum deposit amount is 2000")
            
            
class withdraw(deposit):
    
    def withdraw(self):
        self.withdraw_amount = int(input("Enter the amount to withdraw:"))
        if self.withdraw_amount <= self.balance:
            self.balance -= self.withdraw_amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")
            
class bank(withdraw):
    
    def printdata(self):
        print("______________BANK INFORMATION________________")
        print("Acc no:",self.account_no)
        print("Holder name:",self.holder_name)
        print("Account Type:",self.account_type)
        print("Balance:",self.balance)