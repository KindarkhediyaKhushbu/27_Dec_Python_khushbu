from customer import customer
from Banker import Banker

def show_main_menu():
    print("\n BANKIG SYSTEM")
    print(" 1. Banker Login ")
    print(" 2. Customer Login ")
    print(" 3. Exit ")
    
    choice = int(input("Enter Your Choice(1-3) : "))
    return choice
def Banker_menu():
    print("\nBANKER MENU ")
    print(" 1. Register ")
    print(" 2. Login ")
    print(" 3. Update Customer ")
    print(" 4. View All Customer ")
    print(" 5. Delete All Customer ")
    print(" 6. Exit ")
    choice = int(input("Enter Your Choice(1-6) : "))
    print(choice)
    
    
def customer_menu():
    print("\nCustomer Menu")
    print("1. Register ")
    print("2. Login ")
    print("3. Withdraw Amount ")
    print("4. Deposit Amount ")
    print("5. View Balance ")
    print("6. Logout ")
    choice = input("Enter Your Choice(1-6) : ")
    return choice

def main():
    while True:
        choice = show_main_menu()
        if choice == 1:
            banker_username = input("Enter Banker Username : ")
            banker_password = input("Enter Banker Password : ")
            banker = banker(None, banker_username, banker_password)
            
            