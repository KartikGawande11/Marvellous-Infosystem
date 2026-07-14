'''3: Write a Python program to implement a class named Numbers with the following specifications:

The class should contain one instance variable:

Value

Define a constructor (init) that accepts a number from the user and initializes Value.

Implement the following instance methods:

ChkPrime()returns True if the number is prime, otherwise returns False

ChkPerfect()returns True if the number is perfect, otherwise returns False

Factors()-displays all factors of the number

SumFactors() returns the sum of all factors

Create multiple objects and call all methods.'''
class MathsOperation:

    def __init__(self, Number):
        self.Number = Number

    def ChkPrime(self):
        if self.Number <= 1:
            return False

        for i in range(2, self.Number):
            if self.Number % i == 0:
                return False

        return True

    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Number):
            if self.Number % i == 0:
                sum += i

        return sum == self.Number

    def Factors(self):
        for i in range(1, self.Number + 1):
            if self.Number % i == 0:
                print(i)

    def SumFactors(self):
        sum = 0

        for i in range(1, self.Number + 1):
            if self.Number % i == 0:
                sum += i

        return sum


Number = int(input("Enter your number: "))
Obj = MathsOperation(Number)

print("Prime:", Obj.ChkPrime())
print("Perfect:", Obj.ChkPerfect())

print("Factors:")
Obj.Factors()

print("Sum of Factors:", Obj.SumFactors())
            
    