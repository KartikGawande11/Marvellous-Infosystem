'''2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

Input

(10,15,20,25]

Display

Process ID

Input Number

Factorial'''
import multiprocessing
import time
import os
def Factorial(no):
    print("Process is runing with PID",os.getpid())
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact
            
    

def main():
    Data=[]
    size=int(input("Enter your number size:-"))
    for i in range(size):
        n=int(input())
        Data.append(n)
    start_time=time.perf_counter()
    
    pobj=multiprocessing.Pool()
    result=pobj.map(Factorial,Data)
    pobj.close()
    pobj.join()
    
    print("Result is :-",result)

    
    end_time=time.perf_counter()
    print(f"Time is Allocation:{end_time-start_time:.4f}Second")
    
if __name__=="__main__":
    main()