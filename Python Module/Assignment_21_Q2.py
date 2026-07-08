'''2: Design a Python application that creates two threads.

Thread 1 should calculate and display the maximum element from an list.

Thread 2 should calculate and display the minimum element from the same list.

The list should be accepted from the user.'''
import threading
def Maximum(Data):
    max=0
    for i in Data:
        if i > max:
            max=i
    print("maximum element",max)
    
def Minimum(Data):
    min=0
    for i in Data:
        if i < min:
            min=i
    print("minimum element",min)
    

def main():
    Data=[]
    size=int(input("Enter your element size:-"))
    for i in range(size):
        n=int(input())
        Data.append(n)
         
    
    Thread_1=threading.Thread(target=Maximum,args=(Data,))
    Thread_2=threading.Thread(target=Minimum,args=(Data,))
    
    Thread_1.start()
    Thread_2.start()
    
    Thread_1.join()
    Thread_2.join()
    
if __name__=="__main__":
    main() 