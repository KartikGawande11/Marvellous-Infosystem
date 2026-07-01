#Write a lambda function which accepts two numbers and returns multiplication.
multiplication=lambda no1,no2:no1*no2
def main():
    num1=int(input("enter your First number"))
    num2=int(input("enter your Second number"))
    Ans=num1*num2
    print(" multiplication of the given number",Ans)
if __name__=="__main__":
    main()     
