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
     def __init__(self):
         self.value1=0
         self.value2=0
         self.Add=0
         self.sub=0
         self.mult=0
         self.div=0
         
     def Accept(self):
         self.value1=int(input("Enter your first number :-"))
         self.value2=int(input("Enter your second number :-"))
         
     def Addition(self):
         self.Add=self.value1+self.value2
         print(" Addition :-",self.Add)
         
     def Subtraction(self):
         self.sub=self.value1 - self.value2
         print("Subtraction:-",self.sub)
         
     def Multiplication(self):
         self.mult=self.value1 * self.value2
         print("Multiplication:-",self.mult)
         
     def Division(self):
         self.div=self.value1 / self.value2
         print("Division:-",self.div)
         
         
obj=Arithmetic()
obj.Accept()
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()
         
        