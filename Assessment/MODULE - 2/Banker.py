from database import create_connection

class Banker:
    def __init__(self,name,username,password):
        self.name= name
        self.username = username
        self.password = password
        
        
    def registor(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO customer (name, username, password, balance)valuse(%s,%s,%s)"
        value = (self.name, self.username, self.password)
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
        
    def update_customer(self, customer_id, new_balance):
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE customer SET balance = %s WHERE customer_id = %s"
        cursor.execute(query,(new_balance,customer_id))
        connection.commit()
        print("--CUTOMER UPADATE SUCCUSSFULLY--")
        cursor.close()
        connection.close()
        
    def view_customer(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM customer"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        cursor.close()
        connection.close()
        
    def delete_customer(self,customer_id):
        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(query,(customer_id))
        connection.commit()
        print("-- CTOMER DELETE SUCCUSSFULLY! --")
        cursor.close()
        connection.close()
        