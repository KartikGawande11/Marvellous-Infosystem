#5. Write a program which accepts marks and displays grade.
#Condition Example:
#75 Distinction
#60 First Class
#50 Second Class
# <50-Fail
def Display(no):
    if no>=75:
        print("Distinction")
    elif no>=60:
        print("First Class")   
    elif no>=50:
        print("Second Class")
    else:
        print("Fail")    
def main():
    Marks=int(input("Enter your Marks"))
    Display(Marks)
    pass
if __name__=="__main__":
    main()