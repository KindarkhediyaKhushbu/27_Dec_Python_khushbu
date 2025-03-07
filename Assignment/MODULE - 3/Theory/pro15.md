#### Using the super() function to access properties of the parent class.

- In the given example, The Emp class has an __init__ method that initializes the id, and name and Adds attributes. The Freelance class inherits from the Emp class and adds an additional attribute called Emails. It calls the parent class’s __init__ method super() to initialize the inherited attribute.

```python
class father:
    car: int
    bal: int

    def getdata(self):
        self.car = input("Enter number of car:")
        self.bal = input("Enter bank balance detail:")


class son(father):
    def printdata(self):
        print("Car:", self.car)
        print("Balance:", self.bal)


sn = son()
sn.getdata()
sn.printdata()
```