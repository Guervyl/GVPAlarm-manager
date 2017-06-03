from datetime import datetime
from _datetime import timedelta
from AlarmEntity import AlarmEntity

class AlarmTimeEntity():
    def __init__(self, alarmTimeDao):
        self.id = alarmTimeDao[0]
        self.alarm = AlarmEntity((alarmTimeDao[4],alarmTimeDao[5]))
        dayAlarm = alarmTimeDao[1]
        timeAlarm = str(alarmTimeDao[2])
                
        if len(timeAlarm) == 6:
            hoursAlarm = int(timeAlarm[:2])
            minutesAlarm = int(timeAlarm[2:4])
            secondssAlarm = int(timeAlarm[4:6])
        else:
            hoursAlarm = int(timeAlarm[:1])
            minutesAlarm = int(timeAlarm[1:3])
            secondssAlarm = int(timeAlarm[3:5])
        
        self.datetime = datetime.today()
        self.datetime = datetime(self.datetime.year, self.datetime.month,
               self.datetime.day, hoursAlarm, minutesAlarm, secondssAlarm)
        
        todayWeekday = self.datetime.isoweekday()
        
        # if the alarm is for a day in the next week
        if dayAlarm < todayWeekday:
            self.datetime += timedelta(days=((7 - todayWeekday) + dayAlarm))
        elif dayAlarm > todayWeekday:
            self.datetime += timedelta(days=dayAlarm - todayWeekday)
            
    def __str__(self):
        return "AlarmTimeEntity:: id: " + str(self.id) +"; datetime: "+ str(self.datetime)
        
