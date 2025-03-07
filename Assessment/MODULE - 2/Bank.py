def ragister_Customer(username, password, contactNo, address, accountNo, account_type, account_amount, roll):
        print("AccountHolder Name is :", username)
        print("Your password is:",password)
        print("Your Contact_number is :", contactNo)
        print("Your Address is :", address)
        print("Your Account Number is :", accountNo)
        print("Your Account_type is :", account_type)
        print("Your Account Balance is :",account_amount) 
        print("Your Roll Is :",roll)       
        print("Finally Account is: ",ragister_Customer)
        
def login_Customer(username, password, accountNo, roll):
    print("Account holder username is :",username)
    print("Your password is: ",password)
    print("Your account No is: ",accountNo)
    print("Your roll Is :",roll)
    
def update_all_Customer(username, password, contactNo, Address, Account_no, Account_Type, account_Amount,roll):
        print("AccountHolder Name is :",username)
        print("Your password is:",password)
        print("Your Contact_number is :", contactNo)
        print("Your Address is :", Address)
        print("Your Account Number is :", Account_no)
        print("Your Account_type is :", Account_Type)
        print("Your Account Balance is :",account_Amount)  
        print("Enter Your Roll Customer OR Banker") 
             
        
def View_Customer(name, password, contactNo, Address, Account_no_, Account_Type, account_Amount):
        print("AccountHolder Name is :", name)
        print("Your password is:",password)
        print("Your Contact_number is :", contactNo)
        print("Your Address is :", Address)
        print("Your Account Number is :", Account_no_)
        print("Your Balance is :",account_Amount)
        print("Your Account_type is :", Account_Type)

        
def delete_Customer(C_name, C_password, C_contactNo, C_Address, C_Account_no_, C_Account_Type, C_account_Amount):
        print("AccountHolder Name is :", C_name)
        print("Your password is:",C_password)
        print("Your Contact_number is :", C_contactNo)
        print("Your Address is :", C_Address)
        print("Your Account Number is :", C_Account_no_)
        print("Your Balance is :",C_account_Amount)
        print("Your Account_type is :", C_Account_Type)
        
 
def Amount_of_bank(total_amount,B_Stock):
        print("Total Amount Of bank is :", total_amount)
        print("Total Account Stock is :", B_Stock)
        
def Withdraw_Customer_balance(C_Account_no_,C_acc_Amount):
        print("Your Account Number is :",C_Account_no_)  
        print("Your Balance is ",C_acc_Amount)     
         
def Deposit_Customer_Balance(C_acc_Amount,C_Account_no_):
        print("Your Account Number is :",C_Account_no_)
        print("Your Balance is :",C_acc_Amount)    
        
def Show_balance(balance):
        print("My bank balance is :", balance)           