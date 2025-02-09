# Bank Management System
import asemntmodual as am
from asemntmodual import *

Account_stock = {}
Acc_number = []
Acc_Name=[]
Acc_Type=[]
Acc_balance = []
data  = []

while True:

        print("""Enter Your Choice
      
      1.Add Customer
      2.View Customer
      3.Search Customer
      4.View All Customer
      5.Amount of Bank  
      
        """)

        seq = int(input("Enter your choice (1-5): "))



        if seq == 1:
                    n = int(input("Enter Many Customer You Have to Add: "))
                    for i in range(n):
                                C_name = input("Enter Your Name: ")
                                Acc_Name.append(C_name)
                                print("Your Name  is: ", Acc_Name)
                                C_number = int(input("Enter Your contact Number: "))
                                Acc_number.append(C_number)
                                print("Your Contact_Number  is: ", Acc_number)
                                C_Type = input("Enter Account Type: ")
                                Acc_Type.append(C_Type)
                                print("Your Account Type is: ", Acc_Type)
                                C_acc_Amount =int(input("Enter Your Initial Balance: "))
                                print("Your Initial Balance is: ",C_acc_Amount)
                                Acc_balance.append(C_acc_Amount)
                                print("Your Account Balance is: ", Acc_balance)                    
                                Account_stock[C_number] = {"Name": C_name, "Type": C_Type, "Balance": C_acc_Amount}
                                am.add_Customer(Account_stock, C_name, C_number, C_Type, Acc_balance,C_acc_Amount)
                                
        elif seq == 2:
                                

                                Acc_no = input("Enter Account Number: ")
                                print("Your Account Stock Is :",Acc_no)
                                for Acc_no in Account_stock:
                                        if Acc_no in Account_stock:
                                                print("Your Account Stock Is :",Account_stock)
                                                Account_stock[Acc_no] = {"Name": Account_stock[Acc_no]["Name"], "Type": Account_stock[Acc_no]["Type"], "Balance": Account_stock[Acc_no]["Balance"]}
                                        else:
                                                print("Account not found" , Acc_no)                 
                                am.Search_Customer(Acc_Name, Acc_number, Acc_Type, Acc_balance,C_Type)

        elif seq == 3:          
                                Acc_no = input("Enter Account Number: ")
                                print("Your Account Stock Is :",Acc_no)

                                for  Acc_no in Account_stock:
                                
                                        if Acc_no in Account_stock:
                                        
                                                Account_stock[Acc_no] = {"Name": Account_stock[Acc_no]["Name"], "Type": Account_stock[Acc_no]["Type"], "Balance": Account_stock[Acc_no]["Balance"], "Number": Acc_no}
                                                print("Your Account Stock Is :",Account_stock   )

                                        else:   
                                                ("Account not found" , Acc_no)   

                                am.Search_Customer(Acc_Name, Acc_number, Acc_Type, Acc_balance, Account_stock)

        elif seq == 4:          
                                
                                print("All Customer Info is: ",Account_stock)
                                am.View_all_Customer(Acc_Name, Acc_number, Acc_Type, Acc_balance, Account_stock,C_acc_Amount)
        elif seq == 5:
                                print("Total Amount Of Bank is: ",Acc_balance)
                                total_balance = sum(Acc_balance)
                                print("Total Balance of All Customers: ", total_balance)
                                am.Amount_of_bank(Acc_balance,total_balance)

        

        else:
            print("Invalid Choice!")
