#Write a Python program to create a calculator using functions.
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if  b != 0:
        return a/b
    else:
        print("Error!")
        
def cal():
    print("Select operation")
    print("1.addition")
    print("2.subtraction")
    print("3.multiply")
    print("4.division")
    
    while True:
        choice = (input("Enter your choice(1-4):"))
        
   
        num1 = int(input("Enter first number :"))
        num2 = int(input("Enter second number :"))
            
        if choice == '1':
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif choice == '2':
             print(f"{num1}-{num2}={sub(num1,num2)}")
        elif choice == '3':
            print(f"{num1}*{num2}={mul(num1,num2)}")
        elif choice == '4':
            print(f"{num1}/{num2}={div(num1,num2)}")
        else:
            print("Invaild input! please try again")
cal()
        
        
        
    
    
  