from AlarmTimeDao import AlarmTimeDao
from datetime import datetime
from sched import scheduler
import time
from _datetime import timedelta
from Alarm_exec_thread import AlarmThread

class alarmManager:
    ALARM_RAN_ID = -1
    
    def __init__(self):
        self.alarmTimeEntity = AlarmTimeDao()
    
    def getNextTime(self, datetime):
        timeStr = (datetime.time()).strftime("%H%M%S")
        weekDay = datetime.isoweekday()
        tour = 1
        
        while tour <= 7:
            weekDay = 1 if weekDay > 7 else weekDay
            
            if tour == 1:
                alarmsTimes = self.alarmTimeEntity.selectNext(weekDay, time=timeStr,
                    id=alarmManager.ALARM_RAN_ID)
            else:
                alarmsTimes = self.alarmTimeEntity.selectNext(weekDay, id=alarmManager.ALARM_RAN_ID)
            
            if alarmsTimes is not None:
                break
            
            weekDay += 1
            tour += 1
    
        return alarmsTimes
    
    def execAlarm(self, alarmTimes):
        AlarmThread(alarmTimes).start()
        alarmManager().run()
    
    def run(self, late=0):
        todayReal = datetime.today()
#         todayReal = datetime(2017,6,3, 15, 1, 59)
        today = todayReal
        
        print("today", today)
        if late > 0:
            today -= timedelta(minutes=late)
            print("today late", today)
        
        alarmTimes = self.getNextTime(today)
        
        # close the ddb
        self.alarmTimeEntity.close
        
        if alarmTimes is not None:
            #Call the init alarm script in a separate thread
            AlarmThread(alarmTimes,0).start()
            
            todayWeekday = today.isoweekday()
            alarmDatetime = alarmTimes.datetime
            dayAlarm = alarmDatetime.isoweekday()
            
            if late is 0:
                alarmManager.ALARM_RAN_ID = alarmTimes.id
                
                # Calculate the difference between the ddb time and actual time
                dateSubstract = alarmDatetime - today
                scheduleSeconds = dateSubstract.total_seconds()
                
                print ("Alarm set for ", alarmDatetime)
                print("Alarm will trigger in", scheduleSeconds, "seconds")
                
                # schedule the alarm to execute in the future 
                schedule = scheduler(time.time, time.sleep)
                schedule.enter(scheduleSeconds, 1, self.execAlarm, (alarmTimes,))
                schedule.run()
            else:
                # if the alarm is in the interval, execute it, 
                # else recheck for regular alarm
                if alarmDatetime <= todayReal and alarmDatetime >= today:
                    print("Executing the late alarm right now")
                    print("Going for ordinary alarm")
                    self.execAlarm(alarmTimes)
                else:
                    print("No late alarm set for right now")
                    print("Going for ordinary alarm")
                    alarmManager().run()
        else:
            print("No alarm set")