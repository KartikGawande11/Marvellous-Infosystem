'''Design a Python application that creates two threads named EvenList and OddList.

Both threads should accept a list of integers as input.

The EvenList thread should:

Extract all even elements from the list.

Calculate and display their sum.

The OddList thread should:

Extract all odd elements from the list.

Calculate and display their sum

Threads should run concurrently.'''
import threading
def Even_Number(data):
    sum=0
    print("\nEven Numbers :- ")
    for i in data:
        if i % 2 == 0:
            print(i,end=" ")
            sum +=i
    print("\nSummation of Even number list:-",sum)    
    

def Odd_Number(data):
    sum=0
    print("\nOdd Numbers :- ")
    for i in data:
        if i % 2 != 0:
            print(i, end=" ")
            sum +=i
    print("\nSummation of Odd list:-",sum)


def main():
    
    Data=[]
    size=int(input("Enter your Elements list size :-"))
    for i in range(size):
        no=int(input())
        Data.append(no)
    
    
    t1=threading.Thread(target=Even_Number,args=(Data,))
    t2=threading.Thread(target=Odd_Number,args=(Data,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
if __name__=="__main__":
    main()
    