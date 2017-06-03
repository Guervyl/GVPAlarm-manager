import os
import datetime
import set_rtc_alarm_wake

# Do action when an alarm got executed
def executeAlarm(alarmTime):
    print("exec ")
    os.system("vlc '/media/usb1/Guervyl_backup/Download/to add/new'")
    
# Do action for new alarm
def alarmInit(alarmTime):
    set_rtc_alarm_wake.rtcWake(alarmTime.datetime)
    print("init ")