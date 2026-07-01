#5. Write a lambda function which accepts one number and returns True if number is even otherwise False.
Even=lambda no: no%2==0 
def main():
    num=int(input("Enter your number"))
    Ans=Even(num)
    print("Given number is Even",Ans)
    
if __name__=="__main__":
    main()