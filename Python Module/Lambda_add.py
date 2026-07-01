#8. Write a lambda function which accepts two numbers and returns addition.
Addition=lambda no1,no2:no1+no2
def main():
    num1=int(input("Enter your first number"))
    num2=int(input("Enter your second number"))
    Ans=Addition(num1,num2)
    print("Addition of the given number",Ans)
if __name__=="__main__":
    main()
           