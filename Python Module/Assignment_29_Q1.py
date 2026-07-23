'''Q1) Check File Exists in Current Directory

Problem Statement:

Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:

Demo.txt'''

import os
def main():
    if(os.path.exists("wwf.txt")):
        print(" file exists in the current directory")
    else:
        print(" file exists in not  the current directory")
    pass

if __name__=="__main__":
    main()