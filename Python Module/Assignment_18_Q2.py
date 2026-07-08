#2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
def Maximum(no):
    maximum = no[0]

    for i in no:
        if i > maximum:
            maximum = i

    return maximum
    
def main():
    size=int(input("Enter your number: "))
    Data=[]
    print("Enter the element :")
    for i in range(size):
        no=int(input())
        Data.append(no)
        
    ans=Maximum(Data)    
    print("Maximum of given list: ",ans)
    
    

if __name__=="__main__":
    main()

        