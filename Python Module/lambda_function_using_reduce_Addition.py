#4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

Addition = lambda no1, no2: no1 + no2

def main():
    Data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("Given list:", Data)

    RData = reduce(Addition, Data)

    print("Addition of the given numbers:", RData)

if __name__ == "__main__":
    main()  

