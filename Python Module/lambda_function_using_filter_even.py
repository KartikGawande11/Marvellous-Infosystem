#    #Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.
Even=lambda no:no%2==0
def main():
    Data=[1,2,3,4,5,6,7,8,9,10]
    print("Given Data is ",Data)
    FData=list(filter(Even,Data))
    print("Even number of the given list",FData)
    
if __name__=="__main__":
    main()