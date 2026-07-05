#7. Write a program which accept one number and display below pattern.
def Display(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(j,end=" ")
        print()
    
    

def main():
    num=int(input("Enter your number"))
    Display(num)
    

if __name__=="__main__":
    main()