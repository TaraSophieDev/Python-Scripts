import os
import subprocess as sp
import datetime as dt
import getpass

hour = dt.datetime.now()
cHour = hour.hour

userName = getpass.getuser()
print(userName)

cPath = 'C:/Users/'
path = cPath + userName
if (((dt.datetime.today().weekday() + 1) < 5) and (cHour < 10 and cHour >6)):
    #sp.Popen(path + '/AppData/Local/Microsoft/Teams/current/Teams.exe')
    #sp.Popen('C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE')
    sp.Popen('C:/Program Files/Oracle/VirtualBox/VirtualBox.exe')