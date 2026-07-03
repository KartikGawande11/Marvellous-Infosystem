#1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.
Squares=lambda Data:Data * Data
def main():
    Data=[10,20,30,40,50]
    print("Given Data is",Data)
    MData=list(map(Squares,Data))
    print("squares of each number using Map()",MData)
if __name__=="__main__":
    main()    