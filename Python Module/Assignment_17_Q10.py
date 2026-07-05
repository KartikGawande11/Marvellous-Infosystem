'''10. Write a program which accept number from user and return addition of digits in that number.
Input: 5187934
Output: 37'''
def Digits(no):
    sum=0
    while no>0:
        digits=no%10
        sum=sum + digits
        no=no//10
        
    return sum
    

def main():
    num=int(input("Enter your numbers"))
    Res=Digits(num)
    print("addition of digits in that number.",Res)
    

if __name__=="__main__":
    main()