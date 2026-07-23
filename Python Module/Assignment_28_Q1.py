'''Count Lines in a File

Problem Statement:

Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:

Demo.txt

Expected Output:

Total number of lines in Demo.txt.'''

def main():
    try:
        
        fobj=open("Demo.txt","w")
        print("File get opend")
        
        
        fobj.write("Hii kartik Gawande")
        fobj.write("\n welcome to the coding life")
        print("write successfully")
        
        filename = input("Enter file name : ")

        fobj = open(filename, "r")

        count = 0

        for line in fobj:
         count = count + 1

        print("Total number of lines:", count)

        fobj.close()
            
        
              
    except FileNotFoundError as fobj:
        print("File is not found")


if __name__=="__main__":
    main()