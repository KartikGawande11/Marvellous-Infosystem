def Odd(no):
    for i in range(1,no+1):
        if i %2 !=0:
            print(i)
            
def main():
    num=int(input("Enter your number"))
    Odd(num)
    pass
if __name__=="__main__":
    main()