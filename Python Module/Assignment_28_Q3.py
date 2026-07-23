'''Problem Statement:

Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input: Demo.txt

Expected Output:

Display cach line of Demo.txt one by one.'''

def main():
    try:
        
        
        filename=input("Enter your file :-")
        fobj=open(filename,"r")
        
        print(fobj.read())
        
        fobj.close()
    except FileNotFoundError as fobj:
        print("file is not finde")
    
if __name__=="__main__":
    main()