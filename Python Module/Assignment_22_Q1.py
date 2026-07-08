'''1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 
to N for every element in the list.

Example Input

[1000000,2000000,3000000,4000000]

Expected Output

[333333833333500000,

2666666666667000000,'''
import multiprocessing
import os
import time
def Sumsquare(no):
    print("Process is runing with PID",os.getpid())
    sum=0
    for i in range(1,no+1):
        sum=sum+(i*i)
    return sum
    
def main():
    Data=[]
    size=int(input("Enter your size:-"))
    for i in range(size):
        n=int(input())
        Data.append(n)
    start_time=time.perf_counter()
    
    pojb=multiprocessing.Pool()
    result=pojb.map(Sumsquare,Data)
    pojb.close()
    pojb.join()
    end_time=time.perf_counter()
    
    print("Result is")
    print(result)
    print(f"Time is allocation {end_time-start_time:.4f}Seconds")
if __name__=="__main__":
    main()
        