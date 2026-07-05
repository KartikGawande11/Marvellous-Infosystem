#2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
def Chknum(num):
    if num % 2 == 0:
        print("Number is Even")
        
    else:
        print("Number is Odd")
    


def main():
    num=int(input("Enter your first number"))
    Chknum(num)
    
    
if __name__=="__main__":
    main()