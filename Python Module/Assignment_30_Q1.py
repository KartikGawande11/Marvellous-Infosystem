'''write a program that prints:

Jay Ganesh. every two seconds.

Marvellous Infosystems...

Q

schedule.every(2).seconds.do(...)

Expected output:

Jay Ganesh.

Jay Ganesh.'''

import schedule
import time
import datetime


def Display():
    print("Jay Ganesh",datetime.datetime.now())
def main():
    print("Automation script is start")
    schedule.every(2).seconds.do(Display)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
    print("End of the shudule")
    


if __name__=="__main__":
    main()
