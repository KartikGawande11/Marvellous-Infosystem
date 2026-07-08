'''3. For every number in the given list, count how many prime numbers exist between 
1 and N using multiprocessing Pool.

Example

10000

20000

30000

40000

Display total prime count for each number.'''

import multiprocessing
import time

def prime(Data):
    count = 0
    
    for no in range(2, Data + 1):
    
        for i in range(2, no ):
            if no % i == 0:
                break
        else:
            count = count + 1
    
    return count
        

def main():
    Data=[10000,20000,30000,40000]
    Result = []
        
    start_time=time.perf_counter()
    
    pobj=multiprocessing.Pool()
    
    Result = pobj.map(prime,Data)
    
    pobj.close()
    pobj.join()
    
    print(Result)
    
    end_time=time.perf_counter()
    
    print(f"Time Allocation{end_time-start_time:.4f} second ")
if __name__=="__main__":
    main()
        