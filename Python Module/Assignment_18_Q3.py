#2. Write a program which accept N numbers from user and store it into List. Return Min number from that List.
def Minimum (no):
    minimum  = no[0]

    for i in no:
        if i <  minimum:
            minimum = i

    return minimum
    

def main():
    
    size=int(input("Enter your number: "))
    Data=[]
    print("Enter the element :")
    for i in range(size):
        no=int(input())
        Data.append(no)
        
    ans=Minimum(Data)    
    print("Minimum of given list: ",ans)
    
    

if __name__=="__main__":
    main()
        