'''Design a Python application that creates two separate threads named Even and Odd.

The Even thread should display the first 10 even numbers.

The Odd thread should display the first 10 odd numbers.

Both threads should execute independently using the threading module.

Ensure proper thread creation and execution.'''
    
    
import threading
import time

def EvenNumber():
    print("Even Thread:")
    for i in range(1, 11):
        print(i * 2)

def OddNumber():
    print("Odd Thread:")
    for i in range(10):
        print(i * 2 + 1)

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=EvenNumber, name="Even")
    t2 = threading.Thread(target=OddNumber, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()
    print(f"\nRequired time: {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()