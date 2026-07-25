'''6: Write a program that schedules the following messages:

Use:

Monday at 9:00 AM: Start your weekly goals

Wednesday at 5:00 PM: Review your weekly progress

Friday at 6:00 PM: Weekly work completed

schedule.every().monday.at(...)

schedule.every().wednesday.at(...)

schedule.every().friday.at(...)'''

import time
import schedule
import datetime

def mon():
    print("Start your weekly goals",datetime.datetime.now())
    
def wed():
    print(" Review your weekly progress",datetime.datetime.now())
    
def fri():
    print(" Weekly work completed",datetime.datetime.now())
    
    
def main():
    print("Automation script is starting:")
    schedule.every().monday.at("09:00").do(mon)
    
    schedule.every().wednesday.at("17:00").do(wed)
    
    schedule.every().friday.at("18:00").do(fri)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__=="__main__":
    main()
    
    
    
