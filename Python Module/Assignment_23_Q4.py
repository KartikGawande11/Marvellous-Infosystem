'''4: Write a program that counts how many odd numbers exist between 1 and N.
Input
Data [1000000, 2000000, 3000000, 4000000]
Expected Output Format
Process ID: 1237
Input Number: 1000000
Odd Number Count: 500000'''
import multiprocessing
import time
import os

def CountOdd(Data):
    count=0
    for i in range(1,Data+1,2):
        count=count+1
    print("Odd Number Count:",count)
    return(os.getpid(),count,Data)
    

def main():
    Data=[1000000, 2000000, 3000000, 4000000,5000000]
    Result=[]
    start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(CountOdd,Data)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    
    for pid,number,count in Result:
        print(f"PID of a process :-{pid}")
        print(f"Number :-{number}")
        print(f"Odd Number Count:-{count}")
        print("-"*60)
    print(f" Time Required is :-{end_time-start_time:.5f}")
    

if __name__=="__main__":
    main()