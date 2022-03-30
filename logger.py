from random import randint
import os
import os.path
import time
import datetime
import re
import shutil

totalLogs = 0
sessionID = str(str(time.time()) + "-" + str(randint(0,999999)))


if not os.path.isdir('logs'):
    os.makedirs('logs')
else:
    totalLogs = len(next(os.walk('logs'))[-1])


f = open("logs/" + str(sessionID) + ".txt","x")
firstFile = os.listdir('logs')
firstFile.sort()
firstFile = firstFile[0]
if totalLogs >= 10:
    os.remove('logs/' + str(firstFile))

#####folder/file check ends here#####

#Append log
def log(self):
    global sessionID
    openFile = open("logs/" + sessionID + ".txt", "a")
    dtc = str(datetime.datetime.now())
    print("[" + dtc + "] Logged \"" + self + "\"")
    openFile.write("[" + dtc + "] " + self + " \n")
    openFile.close()
    
def clear(self):
    shutil.rmtree('logs')




#TODO#
#
#Add silent log to prevent printing to terminal
#Add stealth logging (log to different location)
#Add HTTP/FTP logging (log to external/network directories)
#Import/Export logs (export = create ZIP with password, rename extention to custom extention. Password creation/auto-input should be in new module. Password creation should have the same concept as obfusctation. No user input ever required in case of password matters.)



