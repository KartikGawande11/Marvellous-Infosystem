#3. Write a lambda function which accepts two numbers and returns maximum number.
Max=lambda no1,no2:no1 if no1 > no2 else no2
def main():
    num1=int(input("Enter your First number"))
    num2=int(input("Enter your Second number"))
    Ans=Max(num1,num2)
    print("Maximum number is ",Ans)
    
if __name__=="__main__":
    main()