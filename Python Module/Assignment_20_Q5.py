'''5: Design a Python application that creates two threads named Thread1 and Thread2.

Thread1 should display numbers from 1 to 50.

Thread2 should display numbers from 50 to 1 in reverse order.

Ensure that

Thread2 starts execution only after Thread1 has completed.

Use appropriate thread synchronizatio'''
import time
import threading
def displa():
    print("*********************")
    print("Thread_1")
    print("**********************")
    for no in range(1,51):
        print(no)
         

def displa2():
    print("*********************")
    print("Thread_2")
    print("**********************")
    for no in range(50,0,-1):
        print(no)
    

def main():
    start_time=time.perf_counter()
    T1=threading.Thread(target=displa)
    T2=threading.Thread(target=displa2)
    
    T1.start()
    T1.join()
    
    T2.start()
    T2.join()
    end_time=time.perf_counter()
    print(f"Time allocation{end_time-start_time:.5f}")
    
    
    
    
if __name__=="__main__":
    main()