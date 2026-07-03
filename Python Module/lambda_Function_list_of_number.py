#.Write a lambda function using filter() which accepts a list of Even number and also display the count of the Even number 
Number=lambda no:no%2==0 
def main():
    Data=[10,2,3,4,5,6,7,8,9,10,11,2,12,]
    print("Given Data",Data)
    FData=list(filter(Number,Data))
    print("Even number",FData)
    print("count of the even number",len(FData))
    
if __name__=="__main__":
    main()