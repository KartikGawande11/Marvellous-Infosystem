#Write a program which accepts one number and prints cube of that number.
def cube(no):
    a=no*no*no
    return a
    
def main():
    num=int(input("Enter your number"))
    res=cube(num)
    print("Cube of given number",res)
    
if __name__=="__main__":
    main()
    
   