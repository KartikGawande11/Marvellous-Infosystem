#Write a program which contains one lambda function which
# accepts two parameters and return its multiplication
multiplication=lambda no1,no2:no1*no2

def main():
    num1=int(input("Enter your  First Number:"))
    num2=int(input("Enter your second Number:"))
    Ans=multiplication(num1,num2)
    print("Given Multiplication is:",Ans)

if __name__=="__main__":
    main()
    