'''Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even.
Map function will calculate its square. Reduce will return addition of all that numbers.'''
from functools import reduce
Filter=lambda no:no%2==0
Map=lambda no:no*no
Reduce=lambda pr,no:pr+no


def main():
    size=int(input("Enter your number:."))
    Data=[]
    for i in range(size):
        no=int(input("Enter your Elements:."))
        Data.append(no)
    print("Given Data of list",Data)
    
    print("******Filter Fnction*********")
    FData=list(filter(Filter,Data))
    print("After filter Function :.",FData)
    
    print("******Map Function************")
    MData=list(map(Map,FData))
    print("After using Map Function:.",MData)
    
    print("*******Reduce Function***********")
    RData=(reduce(Reduce,MData))
    print("After using reduce function:.",RData)
if __name__=="__main__":
    main()
        