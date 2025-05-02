from database import create_connection

class customer:
    def __init__(self,name,username,password,balance=0):
        self.name= name
        self.username = username
        self.password = password
        self.balance = balance
        
    def registor(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO customer (name, username, password, balance)valuse(%s,%s,%s)"
        value = (self.name, self.username, self.password,self.balance)
        cursor.execute(query,value)
        connection.commit()
        print("---CUSTOMER REGISTER SUCCUSSFULLY---")
        cursor.close()
        connection.close()
        
    def login(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM customer WHERE username = %s, password = %s"
        cursor.execute(query (self.username, self.password))
        result = cursor.fetchone()
        if result:
            print("Login Succussfully")
            return True
        else:
            print("Invalid User!")
            return False
        
    def withdrow(self,amout):
        if self.balance >= amout:
            self.balance >= amout
            connection = create_connection()
            cursor = connection.cursor()
            query = "UPDATE customer SET balance = %s WHERE username = %s"
            cursor.execute(query,(self.balance,self.username))
            connection.commit()
            print("---WITHDROW SUCCUSSFULLY!---")
            cursor.close()
            connection.close()   
        else:
            print("Insufficient funds!")
            
    def deposit(self,amout):
        self.balance += amout
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE customer SET balance = %s WHERE username = %s"
        cursor.execute(query,(self.balance,self.username))
        connection.commit()
        print("--- DEPOSIT SUCCUSSFULY ADD!---")
        cursor.close()
        connection.close()
        
        
    def view_balance(self):
        return self.balance    
            
            
        
        
        
            
    