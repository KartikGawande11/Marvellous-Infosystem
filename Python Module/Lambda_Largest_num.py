#10. Write a lambda functiepagately eyept three numbers and returns largest number
Max=lambda no1,no2,no3 :no1 if no1 > no2 and no1 >no3 else(no2 if no2>no3 else no3)
def main():
    num1=int(input("Enter your First number"))
    num2=int(input("Enter your Second number"))
    num3=int(input("Enter your Second number"))
    Ans=Max(num1,num2,num3)
    print("Maximum number is ",Ans)
    
if __name__=="__main__":
    main()