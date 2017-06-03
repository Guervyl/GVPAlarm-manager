import os
import datetime
import set_rtc_alarm_wake

# Do action when an alarm got executed
def executeAlarm(alarmTime):
    print("executed")
    
# Do action for new alarm
def alarmInit(alarmTime):
    print("init: found a new alarm")
