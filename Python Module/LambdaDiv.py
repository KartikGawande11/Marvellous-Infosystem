#Write a lambda function which accepts one number and returns True if divisible by 5.
divisible=lambda no:True if no%5==0 else False
def main():
    num=int(input("Enter your number"))
    Ans=divisible(num)
    print("number is divisible by 5",Ans)
    
if __name__=="__main__":
    main()
