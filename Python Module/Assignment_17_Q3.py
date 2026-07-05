#3. Write a program which accept one number from user and return its factorial.

def Factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
        
    return fact

def main():
    num=int(input("Enter your number"))
    ans=Factorial(num)
    print("Factorial is",ans)
    
if __name__=="__main__":
    main()