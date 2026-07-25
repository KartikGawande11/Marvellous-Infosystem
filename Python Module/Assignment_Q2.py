'''Write a Python program that monitors the size of a specified file every 30 seconds.

Write the following details into:

FileSizeLog.txt

File path

File size in bytes

Date and time

Handle the situation where the file does not exist.'''
import schedule
import time
import datetime
import os

def FileMonitor(Filepaths):

    currentTime = datetime.datetime.now()

    if os.path.exists(Filepaths):

        size = os.path.getsize(Filepaths)

        fobj = open("FileSizeLog.txt", "a")

        fobj.write("File path : " + Filepaths + "\n")
        fobj.write("File size in bytes : " + str(size) + " bytes\n")
        fobj.write("Date and time : " + currentTime.strftime("%d-%m-%Y %H:%M:%S") + "\n")
        fobj.write("-----------------------------------\n")

        fobj.close()

        print("File information stored")

    else:

        fobj = open("FileSizeLog.txt", "a")

        fobj.write("File does not exist : " + Filepaths + "\n")
        fobj.write("Date and time : " + currentTime.strftime("%d-%m-%Y %H:%M:%S") + "\n")
        fobj.write("-----------------------------------\n")

        fobj.close()

        print("File not found")

def main():

    print("Automation Script is Starting...")

    filepath = input("Enter file path : ")

    schedule.every(30).seconds.do(FileMonitor, filepath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()