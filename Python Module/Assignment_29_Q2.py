'''Q2) Display File Contents

Problem Statement:

Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:

Demo.txt

Expected Output:

Display contents of Demo.txt on console'''


    
import os
def main():
    filename=input("Enter your file name:")
    try:
        fobj=open(filename,"r")
        
        Data=fobj.read()
        print(Data)  
    
    except FileNotFoundError as fobj:
        print("File is not find..")
    

if __name__=="__main__":
    main()