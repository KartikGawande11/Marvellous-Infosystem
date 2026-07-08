'''Design a Python application that creates two threads,

Thread I should compute the sum of elements from a list

Thread 2 should compute the product of elements from the same list

Return the resalts to the main thread and display them.'''
import threading
def sum(Data):
    count=0
    for i in Data:
        count=count+i
    print("Addition = ",count)
    
    
 
def product(Data):
    count=1
    for i in Data:
        count=count*i
    print("product :-",count)


def main():
    Data=[]
    size=int(input("Enter your element size:-"))
    for i in range(size):
        n=int(input())
        Data.append(n)
        
    Thread_I=threading.Thread(target=sum,args=(Data,))
    thread_II=threading.Thread(target=product,args=(Data,))
    
    Thread_I.start()
    thread_II.start()
    
    
    Thread_I.join()
    thread_II.join()

if __name__=="__main__":
    main()    
    