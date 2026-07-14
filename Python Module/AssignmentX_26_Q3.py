'''Write a Python program to implement a class named Arithmetic with the following characteristics:

The class should contain two instance variables: Valuel and Value2.

Define a constructor (init) that initializes all instance variables to 0.

Implement the following instance methods:

Accept()accepts values for Valuel and Value2 from the user.

Addition()-returns the addition of Valuel and Value2.

Subtraction() returns the subtraction of Valuel and Value2.

Multiplication()returns the multiplication of Valuel and Value2.

Division() returns the division of Valuel and Value2 (handle division by zero properly).

Create multiple objects of the Arithmetic class and invoke all the instance methods'''

class Arithmetic:
     # Constructor to initialize instance variables
     def __init__(self):
         self.value1=0
         self.value2=0
         
       # Accept two numbers from the user   
     def Accept(self):
         self.value1=int(input("Enter your first number :-"))
         self.value2=int(input("Enter your second number :-"))
         
     def Addition(self):
         return self.value1 + self.value2
        
         
     def Subtraction(self):
         return self.value1 - self.value2
         
         
     def Multiplication(self):
         return self.value1 * self.value2
        
     def Division(self):
         if self.value2==0:
            return "Division by zero is not possible."
         return self.value1 / self.value2
         
#Object Declartion 1         
obj1=Arithmetic()
print("Accept object 1")
obj1.Accept()

print("Addition :-",obj1.Addition())
print("Subtraction :-",obj1.Subtraction())
print("MUltiplication :-",obj1.Multiplication())
print("Division :-",obj1.Division())        


#Object Declartion 2        
obj2=Arithmetic()
print("\n Accept object 2 ")
obj2.Accept()

print("Addition :-",obj2.Addition())
print("Subtraction :-",obj2.Subtraction())
print("MUltiplication :-",obj2.Multiplication())
print("Division :-",obj2.Division())  