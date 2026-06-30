#Write a program which accepts one number and checks whether it is divisible by 3 and 5
def divisible(no):
    if no%3==0 and no%5==0:
        print("Number is Divisible by 3 and 5")
        
    else:
        print("Number is not Divisible by 3 and 5")
    
    
def main():
    num=int(input("Enter your number"))
    res=divisible(num)
    
    
if __name__=="__main__":
    main()