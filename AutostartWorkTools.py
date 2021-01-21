import os
import subprocess as sp
import datetime as dt

#Detecting directories
homeDirectory = os.environ['USERPROFILE']
programFiles = os.environ['PROGRAMW6432']


weekday = dt.datetime.today().weekday()
hour = dt.datetime.now()
curHour = hour.hour


if (((weekday + 1) < 6) and (6 < curHour < 10)):
    sp.Popen(f'{homeDirectory}/AppData/Local/Microsoft/Teams/current/Teams.exe')
    sp.Popen(f'{programFiles}/Microsoft Office/root/Office16/OUTLOOK.EXE')
    sp.Popen(f'{programFiles}/Oracle/VirtualBox/VirtualBox.exe')
