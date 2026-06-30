#3. Write a program which accepts one number and checks whether it is perfect number or not.
def Perfect_num(no):
    sum=0
    for i in range(1,no):
        if no % i==0:
         sum=sum+i
    if sum==no:
         print("perfect number")
    else:
        print(" number or not perfect.")        
    pass
def main():
    num=int(input("Enter your number"))
    Perfect_num(num)
    
if __name__=="__main__":
    main()