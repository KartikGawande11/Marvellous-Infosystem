#5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element. functools
from functools import reduce 
Maximum=lambda no1,no2: no1 if no1 > no2 else no2
def main():
    Data=[10,20,30,40,50,60,70,80,90,100]
    print("Given Data of list",Data)
    RData=reduce(Maximum,Data)
    print("maximum data is ",RData)
    
if __name__=="__main__":
    main()