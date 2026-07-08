'''5: Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
Input
Data [10, 15, 20, 25]
Expected Task
For every N. calculate:
N!
Expected Output Format
Process ID: 1240
Input Number: 20
Factorial 2432902008176640000'''
import multiprocessing
import os
import time

def Factorial(Data):
    fact=1
    for i in range(1,Data+1):
        fact=fact*i
    print("Factorial",fact)
    print("---------------------------------")
    return(os.getpid(),Data,fact)


def main():
    Data=[10, 15, 20, 25]
    Result=[]
    start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(Factorial,Data)
    pobj.close()
    pobj.join()
    
    end_time=time.perf_counter()
    
    for Pid,Number,fact in Result:
        print(f"Pid of given process :-{Pid}")
        print(f"Number :-{Number}")
        print(f"Factorial :-{fact}")
        print("-"*60)
        
    print(f"Time Required is:-{end_time-start_time:.5f} seconds")
    
    

if __name__=="__main__":
    main()