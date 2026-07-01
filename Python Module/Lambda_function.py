#2. Write a lambda function which accepts one number and returns cube of that number.
Cube=lambda no:no*no*no
def main():
    num=int(input("Enter your number"))
    Ans=Cube(num)
    print("Cube of the given number",Ans)
if __name__=="__main__":
    main()    