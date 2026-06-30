#Write a program which accepts one number and prints all even numbers till that number.
def Even(no):
    for i in range(1,no+1):
        if i % 2 == 0:
            print(i)
    
def main():
    num=int(input("Enter your number"))
    Even(num)
    pass
if __name__=="__main__":
    main()