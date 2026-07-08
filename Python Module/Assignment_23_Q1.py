'''1: Write a Python program using multiprocessing. Pool to calculate the sum of all even numbers
from 1 to N for every number from the given list.
Input
Data [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:
2+4+6+
Expected Output Format
Process ID: 1234
N
Input Number: 1000000
Sum of Even Numbers: 250000500000'''
import multiprocessing
import time
import os

def SumEven(Data):
    sum=0
    for i in range(2,Data+1,2):
        sum=sum+i
    print("Sum of Even Numbers",sum)
    return(os.getpid(),Data,sum)
    
    

def main():
    Data=[1000000, 2000000, 3000000, 4000000]
    Result=[]
    Start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(SumEven,Data)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    
    for pid,num,sum in Result:
        print(f"process ID :-{pid}")
        print(f"Input Number :-{num}")
        print(f"sum of Even Number :-{sum}")
        print("-"*60)
    print(f"\n Time required is:-{end_time-Start_time:.5f}")

if __name__=="__main__":
    main()