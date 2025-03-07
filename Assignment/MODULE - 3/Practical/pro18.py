#Write a Python program to demonstrate the use of super() in inheritance.

class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails

Emp_1 = Freelance(103, "khushbu", "fulrama" , "khushbukindarkhdiya@gmail.com")
print("Id is:", Emp_1.id)
print("Name is:", Emp_1.name)
print(" Address is:", Emp_1.Add)
print("Emails is:", Emp_1.Emails)

