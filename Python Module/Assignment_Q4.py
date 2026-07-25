""":Write a program that copies all.txt files from one directory to another every ten minutes.

The program should:

Accept source and destination directories

Validate both directories

Copy only.txt files

Maintain a log of copied files

Avoid terminating if one file cannot be copied"""

import schedule
import os
import datetime
import time
import shutil

def Display(source, destination):

    if not os.path.isdir(source):
        print("Source directory not found.")
        return

    if not os.path.isdir(destination):
        print("Destination directory not found.")
        return

    fobj = open("CopiesLog.txt", "a")

    fobj.write("\n-------------------------------------\n")
    fobj.write("Copy Operation : " + str(datetime.datetime.now()) + "\n")

    for FolderName, SubFolderName, FileName in os.walk(source):

        for fname in FileName:

            if fname.endswith(".txt"):

                sourcefile = os.path.join(FolderName, fname)
                destfile = os.path.join(destination, fname)

                try:
                    shutil.copy2(sourcefile, destfile)

                    print(fname, "copied successfully.")
                    fobj.write(fname + " copied successfully.\n")

                except Exception as e:

                    print("Cannot copy:", fname)
                    fobj.write(fname + " Copy Failed : " + str(e) + "\n")

    fobj.close()


def main():

    print("Automation Script Started...")

    source = input("Enter source directory : ")
    destination = input("Enter destination directory : ")

    # Use 10 minutes for assignment
    # schedule.every(10).minutes.do(Display, source, destination)

    # Use 5 seconds for testing
    schedule.every(5).seconds.do(Display, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()