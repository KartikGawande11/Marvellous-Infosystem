#Assignment_30_Q2.py
"""Write a Python program that displays the current date and time after every one minute.

Use the datetime module.

Expected output:

Current Date and Time: 25-07-2026 04:30:00 PM"""
import time
import datetime
import schedule

def display():
    
    print("current Data and time:",datetime.datetime.now())
    
def main():
    schedule.every(1).minute.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__=="__main__":
    main()