""": Write a program that reads and displays the contents of a specified text file every minute.

Handle the following conditions:

File does not exist

File is empty

Permission is denied

File cannot be opened"""


import schedule
import time
import datetime
import os

def display(filename):
    
    if not os.path.exists(filename):
        print("File is not Exists:-")
        return
    fobl=open(filename,"r")
    
    data=fobl.read()
    if len(data)==0:
        print("file is empty")
        
    else:
        print("-----------------------------------------","\n")
        print(data)
        print("------------------------------------------")
    
   
    
def main():
    filename=input("Enter your filename:-")
    print("Automation Script starting....")
    
    schedule.every(5).seconds.do(display,filename)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()