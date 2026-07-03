#Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
Divisible=lambda no: no%3==0  and no%5==0

def main():
    Data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print("Given Data is ",Data)
    FData=list(filter(Divisible,Data))
    print("Answer",FData)
    
if __name__=="__main__":
    main()