# Write a program which accepts one number and checks whether it is prime or not.
def Prime(no):
    for i in range(2,no-1):
        if no%i==0:
            return False
def main():
    num=int(input("Enter your number"))
    result=Prime(num)
    if result==False:
        print("Given number is not Prime ")
    else:
        print("Given number is prime")
    
if __name__=="__main__":
    main()