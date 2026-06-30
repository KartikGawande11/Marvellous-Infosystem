#Write a program which accepts one number and prints sum of first N natural numbers.
def Natural(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+i
    print(sum)
    pass
def main():
    num=int(input("Enter your Number"))
    Natural(num)
    
if __name__=="__main__":
    main()