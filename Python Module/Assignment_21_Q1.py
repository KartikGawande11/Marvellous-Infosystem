'''1: Design a Python application that creates two threads named Prime and NonPrime.

COMPUTER ARCHITECTURE

Both threads should accept a list of integers.

The Prime thread should display all prime numbers from the list.

The Non Prime thread should display all non-prime numbers from the list.'''
import threading
def Prime(Data):
    print("Prime Numbers:")
    for no in Data:
        count = 0
        for i in range(1, no + 1):
            if no % i == 0:
                count += 1
        if count == 2:
            print(no)

def Not_Prime(Data):
    print("Non Prime Numbers:")
    for no in Data:
        count = 0
        for i in range(1, no + 1):
            if no % i == 0:
                count += 1
        if count != 2:
            print(no)


def main():
    Data=[]
    size=int(input("Enter your elements list size:-"))
    for i in range(size):
        n=int(input())
        Data.append(n)
    T1=threading.Thread(target=Prime,args=(Data,),)
    T2=threading.Thread(target=Not_Prime,args=(Data,))
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()

if __name__=="__main__":
    main()
