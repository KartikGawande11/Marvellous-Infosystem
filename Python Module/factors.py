#2. Write a program which accepts one number and prints its factors.
def Display(no):
    for i in range(1,no+1):
        if no%i==0:
            print(i)
    
def main():
    num=int(input("Enter your number"))
    Display(num)
    
if __name__=="__main__":
    main()