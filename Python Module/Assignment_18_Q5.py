import MarvellousNum as mn

def ListPrime(data):
    sum = 0
    for i in data:
        if(mn.ChkPrime(i)):
            sum = sum + i
    print("The Sum of Prime Numbers From Your Listr :- ",sum)      

def main():
    n = int(input("Enter no. of Elements :- "))
    data = []
    for i in range(n):
        num = int(input("Enter Element :- "))
        data.append(num)
    ListPrime(data)
if __name__ == "__main__":
    main()