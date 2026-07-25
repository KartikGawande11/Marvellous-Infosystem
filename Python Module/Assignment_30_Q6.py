'''Write a script that schedules the following tasks:

Print Lunch Time! every day at 1:00 PM.

Print Wrap up work every day at 6:00 PM.

Both tasks should be handled by separate functions.'''


import time
import datetime
import schedule

def Display():
    print(" its Lunch Time kartik...!",datetime.datetime.now())
    

def Display1():
    print("its  Wrap up work kartik...!",datetime.datetime.now())
    

def main():
    print("Automation script is starting ")
    schedule.every().day.at("13:00").do(Display) # 1:00 PM.
    schedule.every().day.at("18:00").do(Display1) # 6:00 PM.
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("End of the Automation scripts")
if __name__=="__main__":
    main()