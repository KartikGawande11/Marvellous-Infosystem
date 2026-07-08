'''3. Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function 
# will increase each number by 10. Reduce will return product of all that numbers.'''
from functools import reduce
Filter=lambda no: 70 <= no <= 90
    
Increment=lambda no:no+10
    
Product=lambda pr,no:pr*no

def main():
    size=int(input("enter your number"))
    Data=[]
    for i in range(size):
        value=int(input("Enter your Elements"))
        Data.append(value)
        
    print("Given Data of list",Data)
       
    print("********filter Function*******")
    FData=list(filter(Filter,Data))
    print("After filtaring list.",FData)
    
    print("********Map Function*******")
    mdata=list(map(Increment,FData))
    print("After using  Map function",mdata)
    
    print("********Reduce Function*******")
    Rdata=reduce(Product,mdata)
    print("After using  Map function",Rdata)
    
    
if __name__=="__main__":
    main()