'''2: Design a Python application that creates two threads named EvenFactor and OddFactor.

Both threads should accept one integer number as a parameter.

The EvenFactor thread should:

Identify all even factors of the given number.

Calculate and display the sum of even factors

The OddFactor thread should:

Identify all odd factors of the given number.

Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message "Exit from main'''
import threading

def EvenFactor(no):
    sum = 0
    print("Even Factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            sum = sum + i

    print("Sum of Even Factors :", sum)


def OddFactor(no):
    sum = 0
    print("Odd Factors are:")
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            sum = sum + i

    print("Sum of Odd Factors :", sum)


def main():
    num = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()