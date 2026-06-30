#Write a program which accepts one number and prints multiplication table of that number.
def multiplication(no):
    for i in range(1,11):
        print(no*i)
def main():
    num=int(input("Enter your number"))
    res=multiplication(num)
if __name__=="__main__":
    main()
