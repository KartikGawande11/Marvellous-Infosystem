#1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
def Display(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum
    

def main():
    size=int(input("Enter your number: "))
    Data=[]
    print("Enter the element :")
    for i in range(size):
        no=int(input())
        Data.append(no)
        
    ans=Display(Data)    
    print("Addition of given list: ",ans)
    
    

if __name__=="__main__":
    main()