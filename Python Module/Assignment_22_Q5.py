'''4. Write a program that calculates

105+205+35++N^5

for multiple values of N simultaneously using Pool

Inpat

40000001

Measure total execution'''
import os
import multiprocessing
import time
def simultaneously(Data):
    Ret=0
    for i in range(1,Data):
        Ret=Ret+i**5
        
    return(os.getpid(),Data,Ret)

def main():
    Data=[1000000,2000000,3000000,4000000]
    Result=[]
    start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    Result=pobj.map(simultaneously,Data)
    pobj.close()
    pobj.join()
    print(Result)
    end_time=time.perf_counter()
    
    for pid,num,Ret,in Result:
        print(f"process ID :-{pid}")
        print(f"Input Number :-{num}")
        print(f"sum of 5th:-{Ret}")
        print("-"*60)
    print(f"\n Time required is:-{end_time-start_time:.5f}")
if __name__=="__main__":
    main()    
    