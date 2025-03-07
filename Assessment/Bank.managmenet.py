# Bank managment System

import asemntmodual as am
from asemntmodual import *

Account_stock = {}
Acc_number = []
Acc_Name=[]
Acc_Type=[]
Acc_balance = []
data  = []




while True:
        
        print("""
      
      Choose Your Role
        
                1).Bank Manager
                
                2). Customer 
                
                3). Exit
      
      """)
        
        Choice = int(input("Which Role You Want Choose"))
        print(Choice)



        if Choice == 1:
        
                 print("......Welcome Manager.....")
                 while True:
                
                         print("""Enter Your Choice
                       1).Add Customer
                       2).View Customer
                       3).Search Customer
                       4).View All Customer
                       5).Amount of Bank
                       6).Exit
                         """)
                         seq = int(input("Enter your choice (1-5): "))
                         if seq == 1:
                                     n = int(input("Enter Many Customer You Have to Add: "))
                                     for i in range(n):
                                                 C_name = input("Enter Your Name: ")
                                                 Acc_Name.append(C_name)
                                                 print("Your Name  is: ", Acc_Name)
                                                 
                                                 A_number = int(input("Enter Your Account Number"))
                                                 print("Your Account Number is :",A_number)
                                                 Acc_number.append(A_number)
                                                 
                                                 print("Your Account_number  is: ", Acc_number)
                                                 C_Type = input("Enter Account Type: ")
                                                 Acc_Type.append(C_Type)
                                                 print("Your Account Type is: ", Acc_Type)
                                                 
                                                 C_acc_Amount =int(input("Enter Your Initial Balance: "))
                                                 print("Your Initial Balance is: ",C_acc_Amount)
                                                 Acc_balance.append(C_acc_Amount)
                                                 print("Your Account Balance is: ", Acc_balance)  
                                                                   
                                                 Account_stock[A_number] = {"Name": C_name, "Type": C_Type, "Balance": C_acc_Amount}
                                                 am.add_Customer(Account_stock, C_name, A_number, C_Type, Acc_balance,C_acc_Amount)
                         
                         
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
                         
                         
                         elif seq == 6:
                                         break
                                        
                                
                
                            
        elif Choice == 2:
        
                        print("Welcome our online service")
                
        customer = int(input("Enter Your Choice As Above"))
                        
        if customer == 1:

                        print("""      
                              You Choose Withdraw Section
                              """)
                        Acc_no = int(input("Enter Your Account Number Here"))
                        print("Your Account Number is :",Acc_no)
                        for Acc_no in Account_stock:
                                
                                if Acc_no in Account_stock:
                                        Account_stock[Acc_no]["Balance"] = Acc_balance[Acc_number.index(Acc_no)]
                                        withdraw = int(input("How many You want to withdraw"))
                                        print(withdraw)
                                        
                                        balance = (Account_stock[Acc_no]["Balance"] - withdraw) 
                                        print(balance)
                                        
                                        Acc_balance.append(balance)
                                        Account_stock[Acc_no]["Balance"] = balance
                                        Acc_balance[Acc_number.index(Acc_no)] = balance
                                        print(Account_stock)
                                        
                                else:
                                        print("your Account Number is Wrong")
                                        Withdraw_Customer_balance(Acc_no,withdraw)
                                        
        elif customer == 2:
                        print("""      
                              You Choose Deposit  Section
                              """)    
                        Acc_no = int(input("Enter Your Account Number Here"))
                        print("Your Account Number is :",Acc_no)
                        for Acc_no in Account_stock:
                                if Acc_no in Account_stock:
                                        Account_stock[Acc_no]["Balance"] = Acc_balance[Acc_number.index(Acc_no)]
                                        Deposit = int(input("How many You want to Deposit"))
                                        print(Deposit)
                                        balance = (Account_stock[Acc_no]["Balance"] + Deposit) 
                                        Acc_balance.append(balance)
                                        print(balance)
                                        Account_stock[Acc_no]["Balance"] = balance
                                        Acc_balance[Acc_number.index(Acc_no)] = balance
                                        print(Account_stock)
                                else:
                                        print("your Account Number is Wrong")
                                        Deposit_Customer_Balance(Acc_no,withdraw)
                                        
        elif customer == 3:
                     print("""      
                              Bank balance is 
                        """)
                     
        Acc_no = int(input("Enter Your Account Number Here"))
        print("Your Account Number is :",Acc_no)
        for Acc_no in Account_stock:
                if Acc_no in Account_stock:
                        show = Account_stock[Acc_no] = {balance}
                        print(show)
                else:
                        print("your Account Number is Wrong")
                        Show_balance(show)
                                                          