'''2: Write a Python program to implement a class named Circle with the following requirements:

The class should contain three instance variables: Radius, Area, and Circumference.

The class should contain one class variable named PI, initialized to 3.14.

Define a constructor (init) that initializes all instance variables to 0.0.

Implement the following instance methods:

Accept()-accepts the radius of the circle from the user.

CalculateArea() calculates the area of the circle and stores it in the Area variable.

CalculateCircumference() calculates the circumference of the circle and stores it in the Circumference variable.'''

class circle:
    #class variable
    PI=3.14
    
     # Constructor or instance variables
    def __init__(self):
        self.radius=0
        self.Area=0
        self.Circumference=0
        
    #instance methods:

    def Accept(self):
        self.radius=float(input("Enter your number "))
        
    def CalculateArea(self):
       self.Area= circle.PI*self.radius*self.radius
        
    def CalculateCircumference(self):
        self.Circumference= 2 *  circle.PI * self.radius
    
    
    def Display(self):
        print("Radius :", self.radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)

 # Creating objects
obj=circle()

obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()
    
        
        
        
    