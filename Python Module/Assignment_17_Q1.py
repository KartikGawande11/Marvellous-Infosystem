'''Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction,
Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. 
 Write on python program which call all the functions from Arithmetic module by accepting the parameters from us'''
import Arithmetic_module as Am

def main():
    v1 = int(input("Enter your first number: "))
    v2 = int(input("Enter your second number: "))

    print("Addition is:", Am.Add(v1, v2))
    print("Subtraction is:", Am.Sub(v1, v2))
    print("Multiplication is:", Am.Mult(v1, v2))
    print("Division is:", Am.Div(v1, v2))

if __name__ == "__main__":
    main()

