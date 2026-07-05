#5. Write a program which accept one number for user and check whether number is prime or not.
def prime(no):
    for i in range(2,no+1):
        if (no%i):
            return False
        
    
def main():
    num=int(input("Enter your number"))
    result=prime(num)
    if result==False:
        print("NUmber is prime")
    else:
        print("Number is  not prime")
    pass

if __name__=="__main__":
    main()