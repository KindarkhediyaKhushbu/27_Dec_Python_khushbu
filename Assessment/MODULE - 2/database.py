import mysql.connector

import mysql.connector import error

def create_connection():
    try:
        
        db = mysql.connector.connect(host="localhost", user="root", password="",database="banking system")
        if db.is_connected():
            print("Connection is successfully")
            return db
    except error as e:
        print(e)
        return None
        
        


