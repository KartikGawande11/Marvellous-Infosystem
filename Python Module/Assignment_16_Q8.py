#Write a program which accept number from user and print that number of "*" on screen.
def Display(no):
    for i in range(no):
        print("*",end="")
        
    
def main():
    num=int(input("Enter your number"))
    Display(num)
    
    

if __name__=="__main__":
    main()