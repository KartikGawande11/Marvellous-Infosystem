#3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
def Add(no1,no2):
    Ans=no1+no2
    print("Addition",Ans)
    
def main():
    num1=int(input("Enter your first number"))
    num2=int(input("enter your second number"))
    Add(num1,num2)
    

if __name__=="__main__":
    main()