#Write a lambda function which accepts two numbers and returns minimum number
Minimum=lambda no1,no2:no1 if no1 < no2 else no2
def main():
    num1=int(input("Enter your First number"))
    num2=int(input("Enter your Second number"))
    Ans=Minimum(num1,num2)
    print("Minimum number is ",Ans)
    
if __name__=="__main__":
    main()