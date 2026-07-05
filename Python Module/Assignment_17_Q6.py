#6. Write a program which accept one number and display below pattern.
def Display(no):
    for i in range(no,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    
    

def main():
    num=int(input("Enter your number"))
    Display(num)
    

if __name__=="__main__":
    main()