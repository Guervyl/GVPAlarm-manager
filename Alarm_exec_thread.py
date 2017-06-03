from threading import Thread
import alarm_boot_script

class AlarmThread(Thread):
    def __init__(self, alarmTimeEntity, what=1):
        Thread.__init__(self)
        self.what = what
        self.alarmTimes = alarmTimeEntity
    
    def run(self):
        if self.what is 0:
            alarm_boot_script.alarmInit(self.alarmTimes)
        else:
            alarm_boot_script.executeAlarm(self.alarmTimes)