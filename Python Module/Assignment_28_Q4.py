'''4) Copy File Contents into Another File

Problem Statement:

Write a program which accepts two file names from the user.

First file is an existing file

Second file is a new file

Copy all contents from the first file into the second file.

Input:

ABC.txt Demo.txt'''
def main():
    
        
        Filename=input("Enter your First  file  :-")
        fobj1=open(Filename,"r")
        
        Filename=input("Enter  second your First  file  :-")
        fobj2=open(Filename,"w")
        
        
        Data=fobj1.read()
        fobj2.write(Data)
        
        print("Contents copied successfully.")
        
        fobj1.close()
        fobj2.close()
        


if __name__=="__main__":
    main()