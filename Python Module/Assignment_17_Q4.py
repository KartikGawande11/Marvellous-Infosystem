#Write a program which accept one number form user and return addition of its factors.
def factors(no):
    for i in range(1,no+1):
        if(no%i==0):
            print(i)
    print()
def main():
    num=int(input("enter your number"))
    Ans=factors(num)
    print("factors of given number")
    
if __name__=="__main__":
    main()