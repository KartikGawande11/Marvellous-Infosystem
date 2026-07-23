'''Copy File Contents into a New File (Command Line)

Problem Statement:

Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt. and copies all contents from the given file into Demo.txt.

Input (Command Line):

ABC.txt

Expected Output:

Create Demo.txt and copy contents of ABC.txt into Demo.txt'''

import os 

def main():
    
        ret=input("Enter your file name;-")
        result=os.path.exists(ret)
        
        fobj1=open(ret,"r")
    
        data=fobj1.read()
        
        if result==True:
            print("file exist",data)
        else:
            print("file  not exist")
            
        ret1=open("xyz.txt","w")
        ret1.write(data)
        
        

        
if __name__=="__main__":
    main()