#3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.
def Addition(no1,no2):
    add=no1+no2
    print("Addition",add)
    
def Subtraction(no1,no2):
    sub=no1-no2
    print("Subtraction",sub)
    
def Multiplication(no1,no2):
    mult=no1*no2
    print("Multipliction",mult)
    
def Division(no1,no2):
    div=no1/no2
    print("Division",div)

def main():
    num1=int(input("Enter your first number"))
    num2=int(input("Enter your second number"))
    Addition(num1,num2)
    Subtraction(num1,num2)
    Multiplication(num1,num2)
    Division(num1,num2)
    pass

if __name__=="__main__":
    main()