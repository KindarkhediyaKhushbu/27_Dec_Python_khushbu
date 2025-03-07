"""Write a Python program to check the current position of the file cursor using tell()."""

with open('first.txt', 'r') as file:
   
    file.read(10)

    position = file.tell()
    
    print(f"Current position: {position}")
