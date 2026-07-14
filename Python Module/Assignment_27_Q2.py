'''Write a Python program to implement a class named BankAccount with the following requirements:

The class should contain two instance variables:

Name (Account holder name)

Amount (Account balance)

The class should contain one class variable:

ROI (Rate of Interest), initialized to 10.5

Define a constructor (init) that accepts Name and initial Amount.

Implement the following instance methods:

Display()-displays account holder name and current balance

Deposit() accepts an amount from the user and adds it to balance

Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)

CalculateInterest() calculates and returns interest using formula: Interest (Amount ROI) / 100

Create multiple objects and demonstrate all methods.'''

class BankAccount:
    ROI=10.5
    
    def __init__(self,Name,Amount):
        self.Name =Name
        self.Amount=Amount
        
        
    def Display(self):
        print("Account holder name :- ",self.Name)
        print("Current balance:-",self.Amount)
        
    def Deposit(self):
        amount=int(input("Enter your Amoun for Deposit:-"))
        self.Amount += amount
        print("Amount Deposited Successfully:-")
        print("Current balance:-",self.Amount)
        
        
    def withdraw(self):
        amount=int(input("Enter amount to withdraw"))
        if amount<=self.Amount:
            self.Amount=self.Amount - amount
            print(" withdraw Balance Successful")
            print("Current balance:-",self.Amount)
        else:
            print("Insufficient Balance!")
            
    def CalculateInterest(self):
        Interest=(self.Amount * BankAccount.ROI)/100
        return Interest

print("SBI Bank")   
Name=input("Enter your name:-")
Amount=int(input("Enter your Amount:-"))
obj=BankAccount(Name,Amount) 
obj.Display()
obj.Deposit()
obj.withdraw()
print("Interest",obj.CalculateInterest())



