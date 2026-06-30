def ChkGreater(no1,no2):
    if no1 > no2:
        print("Given numver is greater",no1)
    elif no2 > no1:
        print("Given number is greater",no2)
    else:
        print("Both number are equal")        
    return
def main():
    num1=int(input("Enter your first number"))
    num2=int(input("Enter your second number"))
    res=ChkGreater(num1,num2)
if __name__=="__main__":
    main()