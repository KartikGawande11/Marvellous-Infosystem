"""1: Write a program that creates a new text file every minute.

The filename should contain the current timestamp.

Example:

File_25_07_2026_16_30_00.txt

Write the following information into the file:

Filename

Creation date

Creation time"""


import schedule
import time
import datetime
import os

def display():
    currentTime=datetime.datetime.now()
    filename = currentTime.strftime("File_%d_%m_%Y_%H_%M_%S.txt")
    
    with open(filename, "w") as fobj:
        fobj.write("File Name is:-"+filename +"\n")
        fobj.write("Creation date:-"+ currentTime.strftime("%d-%m-%y")+"\n")
        fobj.write("Creation time:-"+currentTime.strftime("%H_%M_%S")+"\n")
        
        fobj.close()
        print("File create successfully")
        

def main():
    print("Automation Script is sucessfull....")
    schedule.every(1).minute.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()