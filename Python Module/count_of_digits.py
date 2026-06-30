#Write a program which accepts one number and prints count of digits in that number.
def counts(no):
    count=0
    while no>0:
        count=count+1
        no=no//10
    
    print(count)
    
def main():
    num=int(input("Enter your number"))
    counts(num)
    pass
if __name__=="__main__":
    main()