#greater_number.py
def ChkGreater(no1,no2):
    if no1 > no2:
        print("Given number is Gratest",no1)
    else:
        print("Given number is Gratest",no2)    
    
    
num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
    
if __name__=="__main__":
    ChkGreater(num1,num2)