import os
import lazyscript_5
import lazyscript_4
import lazyscript_3
import lazyscript_2
import lazyscript_1
from menu import printer

if __name__ == "__main__":
    mainList = ["my lazy network analysis and monitoring script", "1. Log Parsing", "2. Directory Watching", "3. Port Scanning", "4. Attack Detection", "5. Web Scraping"]
    inp = printer(mainList, 5)
    if inp == 1:
        lazyscript_1.main1()
    elif inp == 2:
        lazyscript_2.main2()
    elif inp == 3:
        lazyscript_3.main3()
    elif inp == 4:
        lazyscrip_4.main4()
    elif inp == 5:
        lazyscript_5.main5()
