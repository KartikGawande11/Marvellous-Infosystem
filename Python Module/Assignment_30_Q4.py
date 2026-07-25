'''4: Create a task that executes every day at 9:00 AM and prints:

Namskar.
Use:

schedule.every().day.at("09:00").do(...)'''

import schedule
import time
import datetime

def display():
    print("Namskar Use:",datetime.datetime.now())
    

def main():
    print("Automation Script starting:")
    schedule.every().day.at("14:32").do(display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()