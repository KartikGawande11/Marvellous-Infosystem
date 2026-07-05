#2. Write a program which accept one number and display below pattern. 5
def Display(no):
    for i in range(no):
        for j in range(no):
            print("*",end=" ")
        print()
    
    

def main():
    num=int(input("Enter your number"))
    Display(num)
    

if __name__=="__main__":
    main()