'''5: Schedule a task that executes every five minutes.

The task should write the current date and time into a file named:

Marvellous.txt

New entries should be appended without removing previous entries.

Example file contents:

Task executed at: 25-07-2026 04:30:00 PM

Task executed at: 25-07-2026 04:35:00 PM'''

import schedule
import time
import datetime

def Schedule():
    fobj=open("Marvellous.txt","a")
    currentTime=datetime.datetime.now()
    fobj.write("Task executed at"+currentTime.strftime("%d-%m-%Y %I:%M:%S %p")+"\n")
    fobj.close()
    
def main():
    print("Automation script is start....!")
    schedule.every(3).seconds.do(Schedule)
    while True:
        schedule.run_pending()
        time.sleep(1)
    pass

if __name__=="__main__":
    main()
    