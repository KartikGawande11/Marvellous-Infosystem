#Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

OddNum=lambda no:no%2 !=0
def main():
    Data=[1,2,3,4,5,6,]
    print("Given Data is ",Data)
    FData=list(filter(OddNum,Data))
    print("Odd number of the given list",FData)
    
if __name__=="__main__":
    main()