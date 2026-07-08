'''5. Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers which are accepted from user.
Filter should filter out all prime numbers. Map function will multiply each number by 2.
Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

Input List 12, 70, 11, 10, 17, 23, 31, 77]

List after filter 12, 11, 17, 23, 311 List after map [4, 22, 34, 46, 62)

Output of reduce 62'''
from functools import reduce
def Filter(no):
    for i in range(2,no):
        if no%i==0:
            return False
        
    return True

def Map(no):
    no=no*2
    return no

def Reduce(no1,no2):
    if no1>no2:
        print(no1)
    else:
        print(no2)
    

def main():
    size=int(input("Enter your number : "))
    Data=[]
    for i in range(size):
        value=int(input("Enter your elements : "))
        Data.append(value)
        
        
    print("Given Data is ",Data)
        
    print("********Filter Function*******")
    FData=list(filter(Filter,Data))
    print("After using Filter Function : ",FData)
    
    
    print("********Map Function***********")
    MData=list(map(Map,FData))
    print("After using Map function",MData)
    
    print("********Reduce Function*********")
    RData=reduce(Reduce,MData)
    print("After using Reduce Function",RData)
    
if __name__=="__main__":
    main()