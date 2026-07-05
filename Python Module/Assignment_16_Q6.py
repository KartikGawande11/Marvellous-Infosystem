#6. Write a program which accept number from user and check whether that number is positive or
def positive(no):
    if no > 0:
        print("number is Positive")
    else:
        print("number is Negative")
    pass

def main():
    num=int(input("Enter your number"))
    positive(num)
    
if __name__=="__main__":
    main()
    