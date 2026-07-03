#6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.
from functools import reduce
minimum=lambda no1,no2:no1 if no1 < no2 else no2
def main():
    Data=[10,20,30,40,50,60,70,80,90,100]
    print("Given Data of the list",Data)
    RData=reduce(minimum,Data)
    print("minimum data:",RData)
    
if __name__=="__main__":
    main()    