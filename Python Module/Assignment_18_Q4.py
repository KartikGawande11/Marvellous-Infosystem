#Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.

def Display(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return i
    return -1
    pass
def main():
    size=int(input("Enter your number"))
    Data=[]
    print("Enter elements")
    for i in range(size):
        no=int(input())
        Data.append(no)
        
    Search=int(input("Enter element to serch "))
    Ans=Display(Data,Search)
    if Ans==-1:
        print("Element is not found")
    else:
        print("number is  found index",Ans)
    pass
if __name__=="__main__":
    main()