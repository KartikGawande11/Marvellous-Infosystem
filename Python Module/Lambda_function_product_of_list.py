#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce
Product=lambda no1,no2:no1*no2
def main():
    Data=[10,20,30,40,50,60,70,80,90,100]
    print("Given Data is :",Data)
    RData=(reduce(Product,Data))
    print("Product of given number is ",RData)
    
if __name__=="__main__":
    main()