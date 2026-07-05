'''9. Write a program which accept number from user and return number of digits in that number.
Output: 7
Input: 5187934'''
def Digits(no):
    count=0
    while no>0:
        count=count+1
        no=no//10
        no=no+no
    return count        
    pass
def main():
    num=int(input("Enter your numbers"))
    Res=Digits(num)
    print("return number of digits in that numbes",Res)
    

if __name__=="__main__":
    main()