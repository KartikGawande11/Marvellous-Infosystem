"""Write a program that deletes all empty files from a specified directory every hour.

The program should:

Scan the directory recursively

Detect files whose size is zero bytes

Delete the empty files

Store deleted file paths in a log file

Handle permission errors

Directry


Test the program only on a sample directory."""
import datetime
import schedule
import time
import os

def display(Direectoryname):
    if  not os.path.exists(Direectoryname):
        print("Direectoryname is not fount")
        return
    if os.path.isdir(Direectoryname):
        logfile="DeletLog "+datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+".txt"
        
        with open(logfile,"a") as fobj:
            fobj.write("-------Empty File ditation log-------------------\n")
            fobj.write("Data and Time.."+ str(datetime.datetime.now())+"\n")
            fobj.write("Direectoryname:"+Direectoryname+"\n")
            
            count=0
    for FolderName,SubFolderName,FileName in os.walk(Direectoryname):
        for file in FileName:
            
            filepath=os.path.join(FolderName,file)
            try:
                if os.path.getsize(filepath)==0:
                    os.remove(filepath)
                    print("Deleted :", filepath)
                    fobj.write("Deleted : " + filepath + "\n")
                    
                    count +=1
            except PermissionError:
                    print("Permission denied :", filepath)
                    fobj.write("Permission denied : " + filepath+ "\n")

            except FileNotFoundError:
                    print("File not found :", filepath)
                    fobj.write("File not found : " + filepath + "\n")

            except Exception as e:
                    print("Error :", e)
                   

        

    print("Log file created successfully.")
            
    
    

def main():
    Direectoryname=input("Enter your directory name:")
    
    schedule.every(3).seconds.do(display,Direectoryname)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()