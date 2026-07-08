'''2: Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.
Input
Data [1000000, 2000000, 3000000, 4000000]
Expected Task
For each number N, calculate:
1+3+5+ + N
Expected Output Format
Process ID: 1235
Input Number: 1000000
Sum of Odd Numbers 250000000000'''
import multiprocessing
import time
import os
def OddNumber(Data):
    sum=0
    for i in range(1,Data+1,2):
        sum=sum+i
            
    print("Sum of Odd Numbers:-",sum)
    return(os.getpid(),Data,sum)
    pass
def main():
    Data=[1000000, 2000000, 3000000, 4000000]
    Result=[]
    Start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(OddNumber,Data)
    pobj.close()
    pobj.join()
    end_time=time.perf_counter()
    
    for pid,num,sum in Result:
        print(f"PID :-{pid}")
        print(f"Num :-{num}")
        print(f"Sum of Odd number :-{sum}")
        print("-"*60)
    print(f"\n Time required is:-{end_time-Start_time:.5f}")
    
    

if __name__=="__main__":
    main()