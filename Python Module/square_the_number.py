#3. Write a program which accepts one number and prints square of that number.
def Square(no):
     a=no*no
     return a   
def main():
    num=(int(input("Enter your number")))
    res=Square(num)
    print("Squar is",res)
       
if __name__=="__main__":
    main()
    