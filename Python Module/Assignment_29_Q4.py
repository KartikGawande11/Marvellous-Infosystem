'''Compare Two Files (Command Line)

Problem Statement:

Write a program which accepts two file names through command line arguments and compares the contents both files.

If both files contain the same contents, display Success

Otherwise display Failure'''

import os

def main():
    
    ret=input("Enter your file :- ")
    result=os.path.exists(ret)
    fobj1=open(ret)
    
    Data=fobj1.read()
    
    
    ret2=input("Enter your second file:-")
    result1=os.path.exists(ret2)
    fobj2=open(ret2)
    
    Data2=fobj2.read()
    
    if Data == Data2:
        print("both files  the same contents:-",Data)
        
    else:
        print("both files  are not the same contents ")


if __name__=="__main__":
    main()