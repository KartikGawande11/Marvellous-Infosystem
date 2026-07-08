'''3: Write a program that counts how many even numbers exist between 1 and N using Pool.map().
Input
Data = [1000000, 2000000, 3000000,
4000000]
Expected Output Format
Process ID: 1236
Input Number: 1000000
Even Number Count: 500000'''
import multiprocessing
import time
import os
def EvenCount(Data):
    count=0
    for i in range(2,Data+1,2):
        count=count+1
    print("Even Number Count :-",count)
    return(os.getpid(),Data,count)
    

def main():
    Data=[1000000, 2000000, 3000000,4000000,5000000]
    Result=[]
    start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(EvenCount,Data)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    
    for Pid,num,count in Result:
        print(f"PID of Process:-{Pid}")
        print(f"Number:-{num}")
        print(f"Even Number Count:-{count}")
        print("-"*60)   
    print(f"\n Time Required is:-{end_time-start_time:.5f}") 

if __name__=="__main__":
    main()