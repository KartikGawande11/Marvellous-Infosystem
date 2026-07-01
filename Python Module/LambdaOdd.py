#Write a lambda function which accepts one number and returns True if number is odd otherwise False.
Odd=lambda no: no%2 !=0 
def main():
    num=int(input("Enter your number"))
    Ans=Odd(num)
    print("Given number is Odd",Ans)
    
if __name__=="__main__":
    main()