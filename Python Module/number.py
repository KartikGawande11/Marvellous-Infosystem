#5.4. Write a program which accepts one number and prints that many numbers starting from 1.
def Number(no):
    for i in range(1,no+1):
        print(i)
        
def main():
    num=int(input("Enter your number"))
    Number(num)
    pass
if __name__=="__main__":
    main()