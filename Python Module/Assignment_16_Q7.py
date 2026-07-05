#7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
def  Divisible(no):
    if no% 5==0:
        return True
    else:
        return False
def main():
    num=int(input("Enter your number"))
    Ans=Divisible(num)
    if Ans:
        print(True)
    else:
        print(False)
    
if __name__=="__main__":
    main()