'''Count Lines in a File

Problem Statement:

Write a program which accepts a file name from the user and counts how many word are present in the file.

Input:

Demo.txt

Expected Output:

Total number of lines in Demo.txt.'''

def main():
    
    try:
        count=0
        
        filename=input("Enter your file name:-")
        fobj = open(filename, "r")
        for line in fobj:
            words=line.split()
            count+=len(words)
        print("Total number of words",count)
        
    except FileNotFoundError as fobl:
        print("file is not finde")

if __name__=="__main__":
    main()