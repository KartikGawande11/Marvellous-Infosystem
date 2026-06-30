#Write a program which accepts one number and prints that many numbers in reverse order.
       
def main():
    num=int(input("Enter your number : "))
    
    for i in range(num, 0 , -1):
        print(i)
    
if __name__=="__main__":
    main()