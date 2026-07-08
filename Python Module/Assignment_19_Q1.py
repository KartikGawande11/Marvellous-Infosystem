#1. Write a program which contains one lambda function which accepts one parameter and 
# return power of two.

power=lambda no:no*no

def main():
    num=int(input("Enter your number :."))
    Ans=power(num)
    print("Power of the given elements:.",Ans)
if __name__=="__main__":
    main()